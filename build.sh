echo "Collecting staticfiles"
python manage.py collectstatic --noinput
echo "Running makemigrations"
python manage.py makemigrations
echo "Running database migrations"
python manage.py migrate --noinput