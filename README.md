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
- it is an abstraction upon your sql queries. 
- you dont have to use raw SQL  
- has their own methods like .all (which is like saying select * in sql)
- it is easy to work with datatypes (to dict)
- autocomplete filterby, query
- you can work with multiple databases like sqlserver, mysql, postgres
- no1 in industry uses raw sql, they use ORMS

## SQL Alchemy
```
from sqlalchemy import create_engine
```

### packages needed
the following is a driver
```bash
pip install pyodbc 
```

the following is an orm. converts to raw sql query then pyodbc returns to sql 
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


1. submit
2. validate
3. add
4. display


# authorization and authentication
## authorization
- what you can do (access level)

## authentiation
- who you are


# business -> data driven
- IoT edge systems/devices that does edge computing. doesnt go to api. 
- use machine learning that then corrects the model 
- products create data
- customer related softwares - CRM (customer relations management)
- CRM tracks flagship customers which are more valuable and -
- lower end members which theyll target with premium/flagship package. Using netflix as an example
- also get data from ERP which is then stored in data lake
- raw data is in data lake. it can be structured and unstructured and semi structured. Its like you just dumping the data from all the softwares 
- you will then take the data and store it on a shelf or freezer because you need to store it for a long time
- you have to organize the data to prepare it for "cooking"
- it is then stored in the data warehouse where you keep organized data.
- once it is organized, people can then visualize the data.
- People will then see commonalities of the data between softwares that grabbed the data.
- use power BI to visualize the data from data warehouse. 
- you can also use machine learning tools for prediction. you can use tools like pandas and numpy (skykit uses pandas and numpy)
- it then can go to data mart. the data mart may only have 2 tables. It is a specific slice of your data warehouse. 
- you can create another app for the data mart. For example a monitoring tool to see if your business is successful. then once again that app will create data and the cycle continues where it goes to the data lake and date warehouse. 

apps create data, data lakes are used to combine , data warehouse s kept organizaed, use tools to visualize or you can take slice of data warehouse (Data Mart) cycle continues

- every app keeps on logging. 

## structured data
- csv files (comma seperrated data)
- excel files


## what is unstructured data
- not in tables
- json files
- images


injestion - data lake consuming data

when you give the data in the data lake logic, it becomes organized. 

creation -> DL -> DW -> DM -> APP
DW -> Pow BI and ML tools

- you can dump anything in the data lake but dont. have some organization to it else it will become a data swamp. Always keep it clean or some logic in what you can dump. 


# SAP
- its like an hr portal
- can deal with sales
- every company needs this


# Governance
- who can see what data
- who can create data
- which app can use/see what data
- it is about access
1. People
2. App
- DevOps is responsible for this 

- Datalake is cheaper than Datawarehouse coz its just storage. But datawarehouse has a database around it.
- Datawarehouse is running all the time - Available - which costs money. Advantage is you can pull it in Power BI or ML tool for further analysis. You can create an app for further analysis. That app will again dump data in the data lake.
- The devops team decide what data they want in the warehouse


# Why did we organize everything
- developer experience
- we now know both ways

# add another page - Process and scalable 
1. Model
2. route
3. app.py (registering)
4. template

# Authentication flow
- browser (react or python templapte) is going to ask backend (node or python itself) for login. With the login API we are gnna send username and password with POST and the backend will verify if it exists or not. If not, it will give an error and you wil remain on the login page. If username and password is valid, you give them a token. The token is important because it validates/authenticates you. The browser stores token because backend will keep asking for token. It is stored in local storage or cookies. 

```bash
pip install flask-login
```


# hashing and encryption
- learn the difference and why we are doing hashing


# when you dont know what kind of columns you'll get when you are trying to insert the data
- 


# Using mongoDB
- How it works
- Database    IMDB
- tables = collections
- rows and columns are called documents in collections

# Advantages of Mongo
- Joins not required (you dont need to normalize the data)
- you can nest documents in mongodb (row in a row) 
- it looks like JSON data
- You can have array of documents as well
- we dont need to do joins because of array of document and nested documents
- you dont need joins because you can store the data as you need it
- in mongodb you can have different key names (not possible in sql coz u have to predefine columns)
- you dont have to define the schema
- you cant have an extra key/column in sql without it applying to all rows(the row can have it as null tho)
- can have consistant data also
- different keys, extra keys, normal
- this is semi structured data
- it is not storing it as JSON but BSON (binary JSON)
- JSON takes more space compared to table
- you are repeating columns/keys in json (JAVASCRIPT OBJECT NOTATION)
- the syntax takes up space
- thats why you use BSON (strips off spaces and quotes and just keeps the data). 
- BSON takes up less space but also has flexibility of JSON

1. no joins required
2. flexible schema/shape of data/blueprint - array of documents, nested documents (embedded documets)
3. gonna store as bson so you dont waste space

# CRUD
Create 
    -  insertOne(data,options)
    - insertMany(data,options)

Read 
    - find(filter,options)
    - findOne(filter, options)
    
Update
    - updateOne(data,options)
    - updateMany(data,options)
    - update one

Delete 
    - deleteOne(data,options)
    - deleteMany(data,options)

## Embedded Documents
- there is a limit of 100 levels of nesting
- max size of document is 16mb

show dbs
db (to know which one you are currenlty in)
use b39we (to switch to a particular tb)
show collections (will show what collections u have)
use (whatever db name)
use alexsanlam
if you ask show dbs then alexsanlam wont show because theres no data yet
db.movies.insertMany({})
db.movies.find()

ObjectID is in BSON
mongodb automatically creates id for u so dont need uuid


connect to vpn
mcirosoft sql server 2016 express sp1
say remove
say next
select all 
next
remove
install the first one new sql stand alone...
i accept
next
next 
select all
next 
next
select grant
next
next

go onto ssms 
connect to sql express 
ALTER SERVER ROLE [sysadmin] ADD MEMBER [MUD\E?????]
GO

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.engine import URL
 
server = 'localhost'
database = 'YourDatabaseName'
username = 'YourUsername'
password = 'YourPassword'
driver_name = "ODBC Driver 17 for SQL Server"
connection_string = f"mssql+pyodbc://{username}:{password}@{server}/{database}?driver={driver_name}"
 
app.config['SQLALCHEMY_DATABASE_URI'] = connection_string
db = SQLAlchemy(app)

mssql+pyodbc://PF3Z9AV0\SQLEXPRESS/moviesdb?driver=ODBC+Driver+17+for+SQL+Server&Encrypt=yes&TrustServerCertificate=no&Connection Timeout=30

to connect to local db - properties for servername and copy the name

# hashing 

```bash
pip install Werkzeug
```

create DockerFile
pip install gunicorn
pip freeze > requirements.txt

