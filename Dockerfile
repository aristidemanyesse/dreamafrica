FROM python:3.9-alpine

RUN apk add --no-cache mariadb-connector-c-dev

COPY requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir -r /app/requirements.txt

COPY ./ /app/

WORKDIR /app/source/

EXPOSE 8000

CMD ["sh", "-c", "python manage.py makemigrations && python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]