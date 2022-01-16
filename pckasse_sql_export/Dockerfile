FROM python:3.9 as dev

ARG INSTALL_DEV=false
ENV PYTHONUNBUFFERED=1

RUN apt-get update && \
  apt-get -y upgrade && \
  apt-get install --no-install-recommends -y postgresql-client && \
  rm -rf /var/lib/apt/lists/*

RUN pip install poetry && poetry config virtualenvs.create false

WORKDIR /code

COPY pckasse_sql_export/pyproject.toml pckasse_sql_export/poetry.lock ./

RUN bash -c "if [ INSTALL_DEV == 'true' ] ; then poetry install --no-root ; else poetry install --no-root --no-dev ; fi"

ENV PYTHONPATH=/code

FROM dev as build

RUN poetry install --no-dev
