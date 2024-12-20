FROM python:3.11-alpine
LABEL authors="dikin"

WORKDIR /app

COPY requirements.txt .

RUN \
  apk add --no-cache postgresql-libs && \
  apk add --no-cache --virtual .build-deps gcc musl-dev postgresql-dev && \
  pip install --no-cache-dir -r requirements.txt && \
  apk --purge del .build-deps

COPY . .

ENV PYTHONUNBUFFERED=1

CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]