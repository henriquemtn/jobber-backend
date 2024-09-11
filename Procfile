web: gunicorn jobber.wsgi --bind 0.0.0.0:$PORT
release: ./manage.py migrate --no-input && ./manage.py collectstatic --noinput