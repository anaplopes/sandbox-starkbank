FROM python:3.10-slim as base

# set env variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install -U pip \
    && apt-get update \
    && apt-get install -y curl build-essential

FROM base as poetry

ENV POETRY_VERSION=1.4.0 \
    POETRY_HOME="/opt/poetry" \
    POETRY_VIRTUALENVS_CREATE=true \
    POETRY_VIRTUALENVS_IN_PROJECT=true

RUN curl -sSL https://install.python-poetry.org | POETRY_VERSION=${POETRY_VERSION} python3 -

ENV PATH="${POETRY_HOME}/bin:$PATH"
RUN poetry config virtualenvs.create ${POETRY_VIRTUALENVS_CREATE}
RUN poetry config virtualenvs.in-project ${POETRY_VIRTUALENVS_IN_PROJECT}

FROM poetry as build

WORKDIR /app

# copy project
COPY src ./src

# install dependencies PIP
# COPY requirements.txt ./requirements.txt
# RUN pip install -r requirements.txt

# install dependencies POETRY
COPY pyproject.toml ./pyproject.toml
RUN poetry install

COPY entrypoint.sh ./entrypoint.sh
RUN chmod +x ./entrypoint.sh

ARG NAME
ENV NAME=$NAME

ENTRYPOINT ["./entrypoint.sh"]
