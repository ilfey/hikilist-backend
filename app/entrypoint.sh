#!/bin/sh

cd app

if [ "$SQL_ENGINE" = "django.db.backends.postgresql" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $SQL_HOST $SQL_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

if [ "$DEBUG" == "true" ]
then
    python3 manage.py runserver 0.0.0.0:8000
else
    python3 manage.py migrate --run-syncdb --noinput

    python3 manage.py collectstatic --noinput

    gunicorn app.wsgi:application --bind 0.0.0.0:8000
fi

exec "$@"