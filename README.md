# arxivapi

This application is an intuitive RESTful API, serving as a facade for the arXiv API. It seamlessly stores query results in a database, making them easily accessible and searchable.

## Architecture
The solution uses Nginx as a reverse proxy and load balancer available via http://localhost. Nginx is followed by a gunicorn web server in combination with uvicorn for the asnyc event loop and serving the FastAPI app following the ASGI standard.

The Redis cache component in the diagram is disabled for this solution.

If you want to send requests to the backend directly, you can do so via http://localhost:8666. The Postgresql database can be reached from the host via http://localhost:5432.

<p align="center">
    <a href="#">
        <img alt="Architecture Workflow" src="https://i.imgur.com/8TEpVZk.png">
    </a>
</p>

## API Endpoints
After starting the application the full API specification can be downloaded as a json, following the OpenAPI Specification from: http://localhost/v1/openapi.json
Here are the main endpoints for your convenience:
```
GET /v1/ping: Health check

GET /v1/arxiv/search: Accepts a title, author, or journal as well as a max_query_results query parameter. Queries the arXiv API and stores the results in a database. Returns the found results to the user sorted by relevance in descending order.
GET /v1/queries: Accepts a query_timestamp_start and an optional query_timestamp_end query parameter and returns all queries made in that time range.
GET /v1/results: Accepts a query_id, items_per_page, and page (number) query parameter and returns the articles found for that query in a paginated fashion.
```

## Features
- The application is fully extensible following as many best practices as possible. Here is a list of used tools:
  - alembic for migrations
  - ruff and black for code formatting
  - mypy for static type checking
  - bandit for security checks
  - coverage for test coverage
  - pytest for testing
  - spell checker for spelling errors in code
  - pre-commit to integrate it all as git hooks and enforce standards
- The backend fully embraces the asynchronous framework. Requests to the arXiv remote and IO to the database are fully async.
- The unit tests run in under half a second. They use a fake arXiv endpoint that generates responses similar to the real arXiv API thereby avoiding any outgoing requests to the arXiv API.
- The unit tests use SQLite as an in memory database that generates all tables on the fly for the tests (in ms). The SQLite database is wrapped in an AsyncSession to simulate the real application as closely as possible.
- A comprehensive Makefile allows many different interactions with the application.
- The API follows REST best practices such as statelessness, API versioning and can be fully extended in any way possible due to the use of advanced FastAPI features like API routers.

## Usage
1. Create a .env file. This will autogenerate a secure DB password for you as well.
`$ bash ./scripts/generate_env.sh`
2. Now run `make` to create the application (using docker compose) and initialize the Postgresql database (using alembic).
Note: If you run the command again it will recreate the entire application, deleting all the database state as well. To shut down the app without losing the database state use `make down` and `make up`to restart the application.
3. (Optional) Execute a sample HTTP GET request against the API using: `make example-query`
4. (Optional) View the persisted results in the database using: `make select-all-from-query`
5. (Optional) Automatic interactive documentation with Swagger UI (from the OpenAPI backend) can be found here: `http://localhost/docs`
6. Run your own queries against the API. For example using `curl -s -X GET "http://localhost/v1/arxiv/search?author=Max+Mustermann&max_query_results=8"`

Here is what you should see if you followed all steps above:

```console
$ make select-all-from-query
                                           query                                           | num_results | status | id |           timestamp
-------------------------------------------------------------------------------------------+-------------+--------+----+-------------------------------
 ArXiv Query: search_query=au:"A. Del Maestro"&amp;id_list=&amp;start=0&amp;max_results=10 |          12 |    200 |  1 | 2024-05-05 23:42:37.788558+00
 ArXiv Query: search_query=au:"Max Mustermann"&amp;id_list=&amp;start=0&amp;max_results=8  |           0 |    200 |  2 | 2024-05-05 23:44:25.628589+00
(2 rows)
```

## Contribute
If you want to contribute pre-commit is a requirement.
If you haven't already done so, download [pre-commit](https://pre-commit.com/) system package and install. Once done, install the git hooks with
```console
$ pre-commit install
pre-commit installed at .git/hooks/pre-commit
```

## Backend local development, additional details

### General workflow
See the [Makefile](/Makefile) to view available commands.

By default, the dependencies are managed with [Poetry](https://python-poetry.org/).

The setup with docker compose allows development without installing anything else besides docker. Tests, linter, and co can be called with the help of the Makefile.

Alternatively you can install all dependencies from `./backend/` with:

```console
$ poetry install
```
The following commands allow you to runt the tests locally
```console
$ poetry shell # creates a virtualenv
$ pytest backend/tests
```


### Nginx
The Nginx webserver can be configured with HTTPS using certbot performing a regular refresh of the TLS certificate. Take a look at the unset environment variables for that.

# Acknowledgements
- The open source developers of all libraries and tools involved!
- arXiv: "Thank you to arXiv for use of its open access interoperability."
- [nickatnight](https://github.com/nickatnight/cookiecutter-fastapi-backend) for the cookiecutter template
