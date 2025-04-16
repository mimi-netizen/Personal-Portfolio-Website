#!/usr/bin/env bash
# exit on error
set -o errexit

pip install -r requirements.txt

# Create necessary directories
mkdir -p media/project_images
mkdir -p staticfiles/media/project_images

python manage.py collectstatic --no-input --clear
python manage.py migrate

# Copy media files
python copy_media.py
