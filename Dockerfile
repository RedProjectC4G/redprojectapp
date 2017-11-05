FROM python:3.5
ADD ./src /srv/www/redproject
WORKDIR /srv/www/redproject
RUN pip install -r requirements.txt
CMD ["python"]
