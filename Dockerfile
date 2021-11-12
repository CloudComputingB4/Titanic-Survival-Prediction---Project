FROM python:3.7

ENV PYTHONUNBUFFERED True

COPY requirements.txt /
RUN pip install -r requirements.txt

COPY . /app

EXPOSE 5000
ENV PORT 5000

WORKDIR /app

ENV API_KEY None

CMD exec gunicorn --bind :$PORT main:app --workers 1 --threads 8 --timeout 0

