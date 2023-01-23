FROM python:alpine
ENV PYTHONUNBUFFERED 1
RUN mkdir app/
WORKDIR /app
COPY requirements.txt .
RUN apk add --no-cache --virtual .build-deps \
     gcc  musl-dev 
RUN pip install -r requirements.txt
COPY . . 
EXPOSE 8000
CMD python manage.py runserver 0.0.0.0:8000
