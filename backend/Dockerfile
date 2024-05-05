FROM python:3.11 as base

ARG env

WORKDIR /tmp

RUN pip install poetry

COPY ./pyproject.toml ./poetry.lock* /tmp/
#COPY ./src/app /tmp/src/app/
#RUN poetry build

RUN poetry export $(test "${env:-dev}" != "prod" && echo "--with dev") \
    -f requirements.txt \
    --output requirements.txt \
    --without-hashes

FROM python:3.11

COPY --from=base /tmp/requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
COPY ./app/ /code/app/

#COPY --from=base /tmp/dist/*.whl /tmp/dist/
#RUN pip install --no-cache-dir /tmp/dist/*.whl && rm /tmp/dist/*.whl

COPY ./alembic.ini /code/alembic.ini
COPY ./logconfig.yml /code/logconfig.yml

WORKDIR /code
ENV PYTHONPATH=/code

EXPOSE 8000
