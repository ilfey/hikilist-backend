FROM python:3.12-alpine as builder

EXPOSE 8000

WORKDIR /srv

COPY . .

RUN pip3 install -r requirements.txt --no-cache-dir

CMD [ "python3", "manage.py", "runserver", "0.0.0.0:8000" ]