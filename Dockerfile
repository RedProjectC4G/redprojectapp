FROM python:3.6

ENV FLASK_ENV dev

COPY . /srv/www/redproject
WORKDIR /srv/www/redproject

RUN pip install pipenv

RUN pipenv install --system

CMD ["python", "manage.py", "run"]
