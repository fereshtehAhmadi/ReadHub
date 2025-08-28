FROM python:3.13-slim AS python-base

ARG BUILD_ENVIRONMENT=production
ENV BUILD_ENVIRONMENT=${BUILD_ENVIRONMENT}

RUN apt-get update && apt-get install --no-install-recommends -y \
    build-essential \
    git \
    libpq-dev \
    postgresql-client \
    gettext \
 && rm -rf /var/lib/apt/lists/*

COPY ./compose/local/django/entrypoint /entrypoint
RUN sed -i 's/\r$//g' /entrypoint
RUN chmod +x /entrypoint

COPY ./requirements /requirements/
RUN pip install --no-cache-dir -r /requirements/${BUILD_ENVIRONMENT}.txt

COPY ./compose/local/django/start /start
RUN chmod +x /start

COPY ./compose/local/django/celery/worker/start /start-celeryworker
RUN sed -i 's/\r$//g' /start-celeryworker
RUN chmod +x /start-celeryworker

COPY ./compose/local/django/celery/beat/start /start-celerybeat
RUN sed -i 's/\r$//g' /start-celerybeat
RUN chmod +x /start-celerybeat

FROM python-base AS python-run-stage

RUN mkdir -p ${APP_HOME}/logs
RUN mkdir -p ${APP_HOME}/src/static

ARG APP_HOME=/app
WORKDIR ${APP_HOME}/src

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

COPY . ${APP_HOME}/

ENTRYPOINT ["/entrypoint"]
