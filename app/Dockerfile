FROM python:3.12-alpine as builder

EXPOSE 8000

WORKDIR /srv

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY . .

COPY ./entrypoint.sh .

RUN dos2unix /srv/entrypoint.sh

RUN chmod +x /srv/entrypoint.sh

RUN pip3 install -r requirements.txt --no-cache-dir

RUN python3 manage.py migrate --run-syncdb --noinput

# CMD [ "python3", "manage.py", "runserver", "0.0.0.0:8000" ]

# CMD ["gunicorn", "app.wsgi:application", "--bind", "0.0.0.0:8000"]

ENTRYPOINT ["/srv/entrypoint.sh"]