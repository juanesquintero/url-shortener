import os
from dotmap import DotMap
from app.shared.utils import get_attr
from pydantic import BaseSettings
from app.shared.constants import Routes, SWAGGER_DESCRIPTION
from logging import DEBUG, getLogger, basicConfig, FileHandler, Formatter, Logger

base_dir = os.path.dirname(os.path.abspath(__file__))

'''LOGGING CONFIG'''
log_format = '%(asctime)s:%(levelname)s:%(name)s:%(message)s'
log_dir = base_dir + '/logs'

def create_logger(level: str):
    level_upper = level.upper()
    file_handler = FileHandler(f'{log_dir}/{level_upper}.log')
    file_handler.setFormatter(Formatter(log_format))
    logger = getLogger(f'{level}_logger')
    logger.setLevel(level_upper)
    logger.addHandler(file_handler)

# GENERAL LOGS (ALL)
getLogger().setLevel(DEBUG)
basicConfig(filename=log_dir+'/GENERAL.log', level=DEBUG, format=log_format)
# ERROR LOGS
create_logger('error')
# INFO LOGS
create_logger('info')

'''END LOGGING CONFIG'''


class Settings(BaseSettings):
    error_logger: Logger = getLogger('error_logger')
    info_logger: Logger = getLogger('info_logger')

    db_host: str = 'db-host'
    db_port: int = 5432
    db_name: str
    db_user: str
    db_password: str

    @property
    def database(self):
        return DotMap({
            'host': self.db_host,
            'port': self.db_port,
            'schema': self.db_name,
            'user': self.db_user,
            'password': self.db_password,
        })

    class Config:
        # case_sensitive = True
        env_file = '.env'


Tags = Routes.__dict__
openapi_tags = get_attr(Tags)

APP_CONFIG = dict(
    title='URL Shortener API',
    version='0.0.1',
    description=SWAGGER_DESCRIPTION,
    contact={
        'name': 'Juan Quintero',
        'url': 'https://github.com/juanesquintero',
        'email': 'juanestquintero@gmail.com',
    },
    openapi_tags=[
        {
            'name': Tags[tag],
            'description': 'Operations with ' + Tags[tag],
        } for tag in openapi_tags
    ]
)
