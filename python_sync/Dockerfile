FROM python:3.11-slim

WORKDIR /app

RUN pip install poetry==1.5.0

COPY . .

RUN poetry install --no-interaction

EXPOSE 3000
ENTRYPOINT ["poetry", "run", "start"]
