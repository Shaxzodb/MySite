![AnVIL Image](https://www.img-studios.com/wp-content/uploads/2016/10/IMG-LOGO-HOMEPAGE.png "AnVIL Portal Image!")

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
---
### CMD or PWSH or GIT BASH

[![Watch the video](https://i.imgur.com/vKb2F1B.png)](https://youtu.be/vt5fpE0bzSY)

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

