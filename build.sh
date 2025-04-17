#!/usr/bin/env bash
# exit on error
set -o errexit

pip install -r requirements.txt

# Create media directory if it doesn't exist
mkdir -p media/project_images

# Copy media files to staticfiles
python manage.py collectstatic --no-input --clear

python manage.py migrate

# Create superuser
DJANGO_SUPERUSER_USERNAME=$ADMIN_USERNAME \
DJANGO_SUPERUSER_PASSWORD=$ADMIN_PASSWORD \
DJANGO_SUPERUSER_EMAIL=$ADMIN_EMAIL \
python manage.py createsuperuser --noinput || true
