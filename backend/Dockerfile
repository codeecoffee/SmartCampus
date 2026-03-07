FROM python:3.14-slim
WORKDIR /app
COPY pyproject.toml uv.lock ./
RUN pip install uv && uv sync
COPY ./app /app
EXPOSE 8000
CMD["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
