#!/bin/sh
set -e

echo "Applying database migrations..."
python src/manage.py migrate --noinput

echo "Collecting static files..."
python src/manage.py collectstatic --noinput

exec "$@"
