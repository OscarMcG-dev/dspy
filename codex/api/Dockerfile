FROM python:3.11-slim

WORKDIR /app

# System deps (optional: sqlite3 CLI for troubleshooting)
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl ca-certificates sqlite3 && rm -rf /var/lib/apt/lists/*

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . ./
ENV PYTHONUNBUFFERED=1
EXPOSE 8000
CMD ["uvicorn", "api.app:app", "--host", "0.0.0.0", "--port", "8000"]
