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
The database will be created automatically with docker volumes using the following file <i>db/sql/creates.sql</i>  and the <i>inserts.sql</i> will populate it with initial test data.
</small>

<br>

<b>pgAdmin</b> GUI on [localhost:8080](http://localhost:8080)

<small>

</small>

## Database

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

## License

This project is licensed under the terms of the MIT license.
