#!/usr/bin/env bash
echo "Collecting static files and migrating database..."
python manage.py collectstatic --noinput
python manage.py migrate
