#!/bin/sh
set -e

echo "Waiting for database..."

# (опционально, но очень желательно — ждём Postgres)
until python manage.py check --database default; do
  echo "DB not ready yet..."
  sleep 2
done

echo "Running migrations..."
python manage.py migrate --noinput

echo "Collecting static..."
python manage.py collectstatic --noinput

echo "Starting server..."
exec gunicorn config.wsgi:application --bind 0.0.0.0:8000