<div align="center">
<h1 align="center" style="text-decoration: none;">URL Shortener</h1>
</div>

<br>

**Source Code**: <a href="https://github.com/juanesquintero/url-shortener" target="_blank"> https://github.com/juanesquintero/url-shortener </a>

---

## About
This project scaffolding for FastAPI framework with Python 3.11 contains:
  - Development Guidelines
  - Clean folder tree
  - FastAPI advanced config & features
  - Docker containerization
  - SQL database connection
  - Testing
  - Linting


<a href="https://nabajyotiborah.medium.com/fastapi-scalable-project-structure-with-docker-compose-45dc3a9fb4c6">
<img height="300" width="500" alt="FastAPI Template" src="https://miro.medium.com/max/1400/1*Thx7VapgMNGDOoLZ2kxBuQ.png">
</a>

<br>

<small>
  All commands in this project must be run on a <b>BASH</b> type terminal.
  (You can use git-bash in windows)
</small>

---

<br>

## Set up local environment

  <b>Docker</b> <br>
  https://www.docker.com/resources/what-container <br>
  https://www.docker.com/get-started


  <b>TechStack</b> <br>

    Python 3.11
    https://www.python.org/

    FastAPI 0.105.0
    https://fastapi.tiangolo.com/

    PostgreSQL 16
    https://www.postgresql.org/



  Clone this repo


  Create <b><i>.env</i></b> file based on the .env.template.

  ```dosini
    ADMIN_EMAIL=admin@url-shortener.com
    DB_PASSWORD=admin123*
  ```

  <small>
    ADMIN_EMAIL for pgAdmin portal login
    DB_PASSWORD for pgAdmin and offcourse for postgresql database password
  </small>

  <b>Containerized</b> <br>

  After install [Docker Desktop](https://www.docker.com/get-started), create the images & instance the containers.

  ```console
  $ docker-compose up
  ```



<b>FastAPI</b> app now is running on [http://localhost:8000](http://localhost:8000)

<small>

</small>

<br>

<b>PostgreSQL</b> database on localhost:5432

<small>

</small>

<br>

<b>pgAdmin</b> GUI on [localhost:8080](http://localhost:8080)

<small>

</small>

## Database

The database will be created automatically with docker volumes using the following file <i>db/sql/creates.sql</i>  and the <i>inserts.sql</i> will populate it with initial test data.

<b>Changes</b> <br>
  If some DDL changes are included to the database is preferred to remove the db container & the data folder (postgres_data) 


---

## Testing

Run tests
```console
$ docker exec url-shortener-api pytest -v tests
```

Run tests & generate html report
```console
$ docker exec url-shortener-api pytest -v --html=tests/report.html --self-contained-html tests
```

Run coverage w/ html Report
```console
$ docker exec url-shortener-api pytest --cov=app --cov-report html:tests/coverage --cov-report term-missing
```

<br>

## API Docs

### Swagger - OpenAPI

Now go to <a href="http://127.0.0.1:8000/docs" class="external-link" target="_blank"> http://localhost:8000/docs </a>

You will see the automatic interactive API documentation (provided by <a href="https://github.com/swagger-api/swagger-ui" class="external-link" target="_blank">Swagger UI</a>):

![Swagger UI](https://fastapi.tiangolo.com/img/index/index-01-swagger-ui-simple.png)


#### GET http://localhost:8000/urls/

Will list the all urls shortened inserted on the db automatically
Also it has 2 query params to get one specific url by original url address or the shorten one 

<b>?short_url=</b><br>
string (query)

<b>?original_url=</b><br>
string (query)

#### GET http://localhost:8000/urls/top

Will list the urls more accesed more clicks in descending order and following th limit given on the query params

<b>?limit=100</b><br>
integer (query)

#### POST http://localhost:8000/urls/shorten

Will post and create the new url with the shorted version of the url using the selected algorithm "Base Conversion Algorithm" for resulition based on PK autoincrement
 
Base Conversion Algorithm
 Convert the unique ID of the long URL into a shorter representation using base conversion techniques. For example, you can convert the decimal representation of the ID into a base58 or base62 encoding, excluding easily confused characters like ‘0’, ‘O’, ‘1’, ‘I’, etc.

<b>?original_url=</b><br>
integer (string)


## License

This project is licensed under the terms of the MIT license.
