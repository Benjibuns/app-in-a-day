## Installing the server
- While in the `app` folder, run the following commands in your terminal 
```
$ pipenv install
```

## Starting the server
- While in the `app` folder, run the following commands in your terminal 
```
$ pipenv shell
(app) python app.py
```

## Create DataBase
- If you need to setup your database you will need to do the following inside a python repl while in your pipenv shell.
- Make sure to be within the `app` folder directory
```
>>> from fileName import db
>>> db.create_all()
```
- This will then add an app.sqlite file to your local computer