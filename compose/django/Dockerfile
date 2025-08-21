FROM python:3.13-slim AS python-base

ARG BUILD_ENVIRONMENT=production
ENV BUILD_ENVIRONMENT=${BUILD_ENVIRONMENT}

RUN apt-get update && apt-get install --no-install-recommends -y \
    build-essential \
    git \
    libpq-dev \
 && rm -rf /var/lib/apt/lists/*

COPY ./requirements /requirements/

RUN pip install --no-cache-dir -r /requirements/${BUILD_ENVIRONMENT}.txt

FROM python-base AS python-run-stage

ARG APP_HOME=/app
WORKDIR ${APP_HOME}

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

COPY . ${APP_HOME}

CMD ["python", "src/manage.py", "runserver", "0.0.0.0:8000"]
