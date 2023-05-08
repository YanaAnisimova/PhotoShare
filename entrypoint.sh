#! /bin/sh

# Collect static files
echo "Collect static files"
python manage.py collectstatic --no-input

## Apply database migrations
#echo "Apply database migrations"
#python manage.py migrate

# Start server
echo "Starting server"
gunicorn dj_project.wsgi:application -b 0.0.0.0:8000