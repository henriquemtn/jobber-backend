web: gunicorn jobber.wsgi --bind 0.0.0.0:$PORT
release: djangoapp/manage.py migrate --no-input && djangoapp/manage.py collectstatic --noinput