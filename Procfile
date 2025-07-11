web: bash -c "python manage.py migrate && gunicorn polling_api.wsgi:application --bind 0.0.0.0:$PORT"
