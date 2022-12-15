
py = py manage.py

# make run
run:
	@$(py) runserver

# make APP=APP_NAME make or make make
make:
	@$(py) makemigrations $(APP)

# make static
static:
	@$(py) collectstatic

# make APP=APP_NAME migrate or make migrate
migrate:
	@$(py) migrate $(APP)

# make APP=NEW_APP_NAME startapp
startapp:
	@$(py) startapp $(APP)

# make superuser
superuser:
	@$(py) createsuperuser

compile:
	@$(py) compilemessages

message:
	@$(py) makemessages
test:
	@$(py) test
