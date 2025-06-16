FROM python:3.13.5-slim-bookworm
WORKDIR /app
COPY api/interact/pyproject.toml api/interact/poetry.lock* /app/
COPY libs/common ./libs/common
RUN pip install poetry && poetry config virtualenvs.create false && poetry install --no-root --only base,kafka
COPY api/interact/. .
CMD ["uvicorn","app.main:app","--host","0.0.0.0","--port","8000"]
