
<p align ="center" width="100%">
<img width="33%" src="https://www.img-studios.com/wp-content/uploads/2016/10/IMG-LOGO-HOMEPAGE.png">
=======


<!-- ![AnVIL Image](https://www.img-studios.com/wp-content/uploads/2016/10/IMG-LOGO-HOMEPAGE.png "AnVIL Portal Image!") -->
</p>



### CMD or PWSH or GIT BASH
#



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

### MAKE-FILE
**py = py manage.py**<br>
@$(py) runserver<br>
@$(py) makemigrations $(APP)<br>
@$(py) collectstatic<br>
@$(py) migrate $(APP)<br>
@$(py) startapp $(APP)<br>
@$(py) createsuperuser<br>

#
> ### Django My Project

# mysite
