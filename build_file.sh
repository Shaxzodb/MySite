@echo [START BUILD]
python manage.py makemigrations
python manage.py migrate
@echo [END BUILD]