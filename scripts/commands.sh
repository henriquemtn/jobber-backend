# O shell irá encerrar a execução do script quando um comando falhar
set -e

echo "PORT is set to: $PORT"

# while ! nc -z $POSTGRES_HOST $POSTGRES_PORT; do
#   echo "🟡 Waiting for Postgres Database Startup ($POSTGRES_HOST $POSTGRES_PORT) ..."
#   sleep 2
# done

# echo "✅ Postgres Database Started Successfully ($POSTGRES_HOST:$POSTGRES_PORT)"

python djangoapp/manage.py collectstatic --noinput
python djangoapp/manage.py makemigrations --noinput
python djangoapp/manage.py migrate --noinput
python djangoapp/manage.py runserver 0.0.0.0:$PORT