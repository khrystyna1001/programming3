FROM python:3.12.7-slim

EXPOSE 8000

WORKDIR /app

COPY requirements.txt .

RUN apt-get update \
    && apt-get install -y build-essential \
    && apt-get install -y libpq-dev

RUN pip install --no-cache-dir -r requirements.txt

COPY new_proj .

ENTRYPOINT [ "python", "manage.py" ]
