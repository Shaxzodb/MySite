@echo [START BUILD]
python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic
@echo [END BUILD]