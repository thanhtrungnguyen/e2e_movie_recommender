FROM python:3.13.5-slim-bookworm
WORKDIR /app
COPY pyproject.toml poetry.lock* /app/
RUN pip install poetry && \
    poetry config virtualenvs.create false && \
    poetry install --no-root --only base,dev
COPY . .
ENTRYPOINT ["airflow"]
