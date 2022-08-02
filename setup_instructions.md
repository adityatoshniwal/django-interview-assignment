# Library Management API

### Python env
Create a virtual env and run:
```shell script
pip install -r requirements.txt
```
And activate the virtual env.

### Run migrations
Run the migrations to prepare the DB using:
```shell script
python manage.py migrate
```

### Run the app
Run the below command to start the app:
```shell script
python manage.py runserver
```

### Swagger UI and API details
Go to the URL and checkout all the APIs.
```
http://localhost:8000/docs/
```
Once you login, copy the access token, click on authorize and add the token to jwtAuth.

### User signup
To signup as `Librarian` use role id as `1` and for `Member` use role id as `2` 