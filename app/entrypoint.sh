#!/bin/sh

cd app

if [ "$DEBUG" == "true" ]
then
    python3 manage.py runserver 0.0.0.0:8000
else
    python3 manage.py migrate --run-syncdb --noinput

    python3 manage.py collectstatic --noinput

    gunicorn app.wsgi:application --bind 0.0.0.0:8000
fi

exec "$@"