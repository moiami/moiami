FROM python:3.12-slim AS builder

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    gcc \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

RUN pip install uv

COPY pyproject.toml uv.lock ./

RUN uv sync --locked --no-dev --no-install-project
COPY . .

FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PATH="/app/.venv/bin:$PATH"

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    libpq5 \
    netcat-openbsd \
    && rm -rf /var/lib/apt/lists/*

RUN useradd --create-home --shell /bin/bash appuser

COPY --from=builder /app /app

RUN mkdir -p /app/staticfiles && \
    chown -R appuser:appuser /app

USER appuser

EXPOSE 8000

HEALTHCHECK --interval=30s --timeout=5s --start-period=20s --retries=3 \
CMD python manage.py check || exit 1

CMD sh -c "until nc -z \"$DB_HOST\" \"$DB_PORT\"; do sleep 2; done && python manage.py migrate --noinput && python manage.py collectstatic --noinput && exec gunicorn config.wsgi:application --bind 0.0.0.0:8000 --workers 4 --threads 2 --timeout 120"