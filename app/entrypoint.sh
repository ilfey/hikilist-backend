#!/bin/sh

python3 app/manage.py migrate --run-syncdb --noinput

python3 app/manage.py collectstatic --noinput

cd app

gunicorn app.wsgi:application --bind 0.0.0.0:8000

exec "$@"