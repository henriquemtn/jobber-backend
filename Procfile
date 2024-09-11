web: gunicorn djangoapp.wsgi --bind 0.0.0.0:$PORT
release: python3 djangoapp/manage.py migrate --no-input && python3 djangoapp/manage.py collectstatic --noinput