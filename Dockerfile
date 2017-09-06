FROM tiangolo/uwsgi-nginx-flask:python3.6

WORKDIR /app
COPY ./app/requirements.txt /app
RUN pip install -r requirements.txt

COPY ./app /app



