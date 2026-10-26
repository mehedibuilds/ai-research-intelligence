FROM python:3.11-slim
ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1 PYTHONPATH=/app/apps/api/src
WORKDIR /app
COPY pyproject.toml README.md ./
COPY apps/api/src ./apps/api/src
RUN pip install --no-cache-dir .
CMD ["uvicorn", "pip_api.main:app", "--host", "0.0.0.0", "--port", "8000"]