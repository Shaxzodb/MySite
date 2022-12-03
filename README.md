    py = py manage.py
    run:
	    @$(py) runserver
    make:
	    @$(py) makemigrations $(APP)
    static:
	    @$(py) collectstatic
    migrate:
	    @$(py) migrate $(APP)
    createapp:
	    @$(py) startapp $(APP)
    superuser:
	    @$(py) createsuperuser
-------
### CMD or PWSH or GIT BASH
------
```cmd
make run
```
```cmd
make APP=APP_NAME make or make make
```
```cmd
make static
```
```cmd
make APP=APP_NAME migrate or make migrate
```
```cmd
make APP=NEW_APP_NAME startapp
```
```cmd
make superuser
```

