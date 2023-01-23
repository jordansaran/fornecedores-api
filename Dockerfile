FROM python:3.10.9-slim-bullseye
WORKDIR /usr/src/app
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN pip install --upgrade pip
COPY ./requirements.txt /usr/src/app/requirements.txt
COPY ./.env.example /usr/src/app/.env
RUN pip install -r requirements.txt
COPY . /usr/src/app/
RUN chmod -R 777 /usr/src/app/

CMD ["flask", "db", "upgrade"]

EXPOSE 5000