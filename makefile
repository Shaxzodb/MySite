py = py manage.py

# make run
run:
	@$(py) runserver

test:
	@$(py) test

# make APP=NEW_APP_NAME app
app:
	@$(py) startapp $(APP)

# make APP=APP_NAME make or make make
make:
	@$(py) makemigrations $(APP)

# make static
static:
	@$(py) collectstatic

# make APP=APP_NAME migrate or make migrate
migrate:
	@$(py) migrate $(APP)

# make superuser
superuser:
	@$(py) createsuperuser

compile:
	@$(py) compilemessages

message:
	@$(py) makemessages --all