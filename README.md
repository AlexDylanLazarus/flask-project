# Setup

## Virtual env

```bash
python -m venv myenv  
```

## Activate
```bash
.\myenv\Scripts\activate   
```

## Git
```bash
git init
```

## Gitignore

Add `.gitignore`
Add myenv in that file

## create repo in github
1. `git add .`
2. `git commit -m "initialized flask project"`
3. Push to GitHub

## Installing flask
[make sure you env is activated](https://flask.palletsprojects.com/en/3.0.x/installation/)
```bash
pip install flask
```

# Why flask

html to talk to databse you need a backend. python will be the backend. 
python query the db with sql then db sends the query back to python and python sends it as json to frontend.
REST API - GET (READING DATA), POST (CREATING DATA), PUT(UPDATING DATA), DELETE(DELETING DATA). Dont criss-coss these things. frontend asks and receives in json.
python converts the frontend requests (get, post...) to sql query then eventually sends it back to frontend as json.


- So flask is a framework that runs in python. give a very nice dx to build get, post, put, and delete. There are existing tools in flask to build those.
- it is a micro framework.
- gives ready made tools to implement REST API
- it is called micro because it uses django (which is full fletched )
- freedom with flask but django is a one stop solution. It is pre made.
- flask is as powerful as django
- flask is lightweight

# How to run flask
```bash
 flask --app main run
```

only if your main file is called app you can do the following:
```bash
 flask run
```

- every time you make a change, you have to restart the server with `ctrl + C`

if you don't want to restart every time you can do the following:
```bash
 flask run --debug
```

so you just save and refresh your browser

to change address

```bash
flask run --host=0.0.0.0
```

# REST API/ENDPOINT
- CRUD 

Traditional way to do things is  to send an html file. 

# Jinja 2 
- creates html templates for you

# check packages(take snapshot of packages) 
```bash
pip freeze > requirements.txt
```


# to install snapshot/ all dependencies
- whoever wants to clone it they can just use one line:
```bash
pip install -r requirements.txt
```

as you install more packages, you will need to take a snapshot of the packages

#to check currently installed
```bash
pip freeze
```

# ORM (object relational mapping)
- you dont have to use raw SQL  
- has their own methods like .all (which is like saying select * in sql)
- it is easy to work with datatypes
- autocomplete: 
- you can work with multiple databases like sqlserver, mysql, postgres
- no1 in industry uses raw sql, they use ORMS

## SQL Alchemy
```
from sqlalchemy import create_engine
```

### packages needed
```bash
pip install pyodbc
```
```bash
pip install SQLAlchemy
```

```bash
pip install flask_sqlalchemy
```

```bash
pip install python-dotenv
```

# blue print 
- to break the long file down

## advantages include:
- modularity
- scalability
- reusablity


# base html/ template inheritence
- 

# Validations
- need criteria for certain form to be valid
- we want clean data in the database (dont want to store junk data)
- improving user experience (allowing them to correct themselves)
- business rules
- security
- error prevention
- data integrity


## Can use flask WTF
- can use CSRF token. it is like a stamp that makes it legit. 
- on every form we can have this stamp/seal
- so for example if you have a payment form, where you have to send the name etc. In our bank webpage we will have an extra seal. The hackers wont have the seal so if hackers try to connect to the db they can't. We are safeguarding our users.


```bash 
pip install Flask-WTF
```
