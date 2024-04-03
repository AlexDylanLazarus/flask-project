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



