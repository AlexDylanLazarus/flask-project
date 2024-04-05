

```js
show dbs
db (to know which one you are currenlty in)
use b39we (to switch to a particular db and if it dont exist it creates for you)
show collections (will show what collections u have)
use <whatever db name>
use alexsanlam
if you ask show dbs then alexsanlam wont show because theres no data yet
db.movies.insertMany([
  {
    "id": "99",
    "name": "Vikram",
    "poster": "https://m.media-amazon.com/images/M/MV5BMmJhYTYxMGEtNjQ5NS00MWZiLWEwN2ItYjJmMWE2YTU1YWYxXkEyXkFqcGdeQXVyMTEzNzg0Mjkx._V1_.jpg",
    "rating": 8.4,
    "summary": "Members of a black ops team must track and eliminate a gang of masked murderers.",
    "trailer": "https://www.youtube.com/embed/OKBMCL-frPU"
  },
  {
    "id": "100",
    "name": "RRR",
    "poster": "https://englishtribuneimages.blob.core.windows.net/gallary-content/2021/6/Desk/2021_6$largeimg_977224513.JPG",
    "rating": 8.8,
    "summary": "RRR is an upcoming Indian Telugu-language period action drama film directed by S. S. Rajamouli, and produced by D. V. V. Danayya of DVV Entertainments.",
    "trailer": "https://www.youtube.com/embed/f_vbAtFSEc0"
  },
  {
    "id": "101",
    "name": "Iron man 2",
    "poster": "https://m.media-amazon.com/images/M/MV5BMTM0MDgwNjMyMl5BMl5BanBnXkFtZTcwNTg3NzAzMw@@._V1_FMjpg_UX1000_.jpg",
    "rating": 7,
    "summary": "With the world now aware that he is Iron Man, billionaire inventor Tony Stark (Robert Downey Jr.) faces pressure from all sides to share his technology with the military. He is reluctant to divulge the secrets of his armored suit, fearing the information will fall into the wrong hands. With Pepper Potts (Gwyneth Paltrow) and Rhodes (Don Cheadle) by his side, Tony must forge new alliances and confront a powerful new enemy.",
    "trailer": "https://www.youtube.com/embed/wKtcmiifycU"
  },
  {
    "id": "102",
    "name": "No Country for Old Men",
    "poster": "https://upload.wikimedia.org/wikipedia/en/8/8b/No_Country_for_Old_Men_poster.jpg",
    "rating": 8.1,
    "summary": "A hunter's life takes a drastic turn when he discovers two million dollars while strolling through the aftermath of a drug deal. He is then pursued by a psychopathic killer who wants the money.",
    "trailer": "https://www.youtube.com/embed/38A__WT3-o0"
  },
  {
    "id": "103",
    "name": "Jai Bhim",
    "poster": "https://m.media-amazon.com/images/M/MV5BY2Y5ZWMwZDgtZDQxYy00Mjk0LThhY2YtMmU1MTRmMjVhMjRiXkEyXkFqcGdeQXVyMTI1NDEyNTM5._V1_FMjpg_UX1000_.jpg",
    "summary": "A tribal woman and a righteous lawyer battle in court to unravel the mystery around the disappearance of her husband, who was picked up the police on a false case",
    "rating": 8.8,
    "trailer": "https://www.youtube.com/embed/nnXpbTFrqXA"
  },
  {
    "id": "104",
    "name": "The Avengers",
    "rating": 8,
    "summary": "Marvel's The Avengers (classified under the name Marvel Avengers\n Assemble in the United Kingdom and Ireland), or simply The Avengers, is\n a 2012 American superhero film based on the Marvel Comics superhero team\n of the same name.",
    "poster": "https://terrigen-cdn-dev.marvel.com/content/prod/1x/avengersendgame_lob_crd_05.jpg",
    "trailer": "https://www.youtube.com/embed/eOrNdBpGMv8"
  },
  {
    "id": "105",
    "name": "Interstellar",
    "poster": "https://m.media-amazon.com/images/I/A1JVqNMI7UL._SL1500_.jpg",
    "rating": 8.6,
    "summary": "When Earth becomes uninhabitable in the future, a farmer and ex-NASA\n pilot, Joseph Cooper, is tasked to pilot a spacecraft, along with a team\n of researchers, to find a new planet for humans.",
    "trailer": "https://www.youtube.com/embed/zSWdZVtXT7E"
  },
  {
    "id": "106",
    "name": "Baahubali",
    "poster": "https://flxt.tmsimg.com/assets/p11546593_p_v10_af.jpg",
    "rating": 8,
    "summary": "In the kingdom of Mahishmati, Shivudu falls in love with a young warrior woman. While trying to woo her, he learns about the conflict-ridden past of his family and his true legacy.",
    "trailer": "https://www.youtube.com/embed/sOEg_YZQsTI"
  },
  {
    "id": "107",
    "name": "Ratatouille",
    "poster": "https://resizing.flixster.com/gL_JpWcD7sNHNYSwI1ff069Yyug=/ems.ZW1zLXByZC1hc3NldHMvbW92aWVzLzc4ZmJhZjZiLTEzNWMtNDIwOC1hYzU1LTgwZjE3ZjQzNTdiNy5qcGc=",
    "rating": 8,
    "summary": "Remy, a rat, aspires to become a renowned French chef. However, he fails to realise that people despise rodents and will never enjoy a meal cooked by him.",
    "trailer": "https://www.youtube.com/embed/NgsQ8mVkN8w"
  },
  {
    "name": "PS2",
    "poster": "https://m.media-amazon.com/images/M/MV5BYjFjMTQzY2EtZjQ5MC00NGUyLWJiYWMtZDI3MTQ1MGU4OGY2XkEyXkFqcGdeQXVyNDExMjcyMzA@._V1_.jpg",
    "summary": "Ponniyin Selvan: I is an upcoming Indian Tamil-language epic period action film directed by Mani Ratnam, who co-wrote it with Elango Kumaravel and B. Jeyamohan",
    "rating": 8,
    "trailer": "https://www.youtube.com/embed/KsH2LA8pCjo",
    "id": "108"
  },
  {
    "name": "Thor: Ragnarok",
    "poster": "https://m.media-amazon.com/images/M/MV5BMjMyNDkzMzI1OF5BMl5BanBnXkFtZTgwODcxODg5MjI@._V1_.jpg",
    "summary": "When Earth becomes uninhabitable in the future, a farmer and ex-NASA\\n pilot, Joseph Cooper, is tasked to pilot a spacecraft, along with a team\\n of researchers, to find a new planet for humans.",
    "rating": 8.8,
    "trailer": "https://youtu.be/NgsQ8mVkN8w",
    "id": "109"
  }
]
)
db.movies.find({"id": "100"})
db.collection.find({
  rating: 8
})
// comparisson operators
db.collection.find({
  rating: {
    "$gt": 8 //double quotes on left side is optional
  }
})
db.collection.find({
  rating: {
    "$lt": 8
  }
})
db.collection.find({
  rating: {
    "$gte":  8
  }
})
db.collection.find({
  rating: {
    "$lte": 8
  }
})
db.collection.find({
  rating: {
    "$in": [
      8.4,
      7,
      8.1
    ]
  }
})
db.collection.find({
  rating: {
    "$nin": [
      8.4,
      7,
      8.1
    ]
  }
})
db.movies.find({}).count
```

```sql
SELECT * FROM movies WHERE id = '100';

SELECT * FROM collection WHERE rating = 8;

SELECT * FROM collection WHERE rating > 8;

SELECT * FROM collection WHERE rating < 8;

SELECT * FROM collection WHERE rating >= 8;

SELECT * FROM collection WHERE rating <= 8;

SELECT * FROM collection WHERE rating IN (8.4, 7, 8.1);

SELECT * FROM collection WHERE rating NOT IN (8.4, 7, 8.1);
```

# hashing and encryption
Basically, encryption is the process of scrambling plaintext into unreadable ciphertext, which you can decrypt with a relevant key, while hashing turns plain text into a unique code, which can't be reverted into a readable form.


- encryption converts to unreadable text and is reversable
- hashing converts to fixed size string of characters and used for password storage

# encryption
- its weak coz u can convert back to original form 
- if you know the decryption key then you can decrypt faster


# hashing 
- can't reverse back
- set length
- highly sensitive 
- it is the fingerprint of the input
- same input gives same hash value(output)

example:
input -> hash function -> hash value (10 digit number)
- if you change even one letter in your input the hash value(output) will be different
- it is highly sensitive and unique
- hash value is the fingerprint of the file so you cant reverse it
- another example, they use software that gives hash value for your download 
- put it through checksum function
- a hacker would try to get your password from common hash values . So they look at common passwords like 12345678. Then they hash those common passwords until it matches the hash value
- how to beat hacker, dont let the hacker make the move they wanna make
- salting - you add a random string to the password before hashing it
- salt value is the random string you give

algorithm + algorithm options(eg cost) + salt = hashed password

## check_has () behind the scenes
password@123 + x5qxqrc1r0PvqWJr -> scypt:password@123x5qxqrc1r0PvqWJr


# Back to mongoDB
## Projections
<!-- db.movies.find({}).count -->

inclusion projection (only say things u need to be included)
db.movies.find({},{name:1.rating:1})

exclusion projection 
db.movies.find({},{summary:0,trailer:0})

db.movies.find({}, {_id:0, name:1 , rating:1}) #_id is the only exception when mixing

db.collection.find({
  rating: {
    "$gt": 8.5 //double quotes on left side is optional
  }
},{_id:0,name:1,rating:1})

db.collection.find({}).sort({rating:1}) gives ascending sort
db.collection.find({}).sort({rating:-1}) gives descending sort
db.movies.find({},{_id:0,name:1,rating:1}).sort({name:1, rating:-1})
db.movies.find().limit(3)
db.movies.find({},{_id:0,name:1,rating:1}).limit(3).skip(3)

# Data types in mongo db
Text - "person 1"
Boolean - true
Integer(int 32) - 36
NumberLong - 10000000000
Number Decimal - 14.36
ObjectId - ObjectID("252fd")
ISODate - ISODATE("2019-05-66)
Embedded - nested documents
- array of documents

## Choose wisely

SQL
Fast - throws the book
slow search where he kept it
It is a balanced database so everyone can use it
faster at insertions

MongoDB
slow Orders the books (takes time)
fast pick it from library
- slower at inserting
- Can use it for twitter coz reading is faster
- so use nosql when you have read intensive apps so generally social media apps

- insertion heavy apps - Google docs, Share market (trading. JSE), Weather app, 

Amazon uses multiple databases coz it depends upon the scenario



## Aggregation 
```js
db.orders.insertMany([
{ _id: 0, productName: "Steel beam", status: "new", quantity: 10 },
{ _id: 1, productName: "Steel beam", status: "urgent", quantity: 20 },
{ _id: 2, productName: "Steel beam", status: "urgent", quantity: 30 },
{ _id: 3, productName: "Iron rod", status: "new", quantity: 15 },
{ _id: 4, productName: "Iron rod", status: "urgent", quantity: 50 },
{ _id: 5, productName: "Iron rod", status: "urgent", quantity: 10 }
])
```

```sql
SELECT productName as _id, SUM(quantity) as totalQuanity from orders where status='urgent' group by productName
```

```js
db.orders.aggregate([{$match:{status:'urgent'}},{$group:{_id:"$productName" , totalUrgentQuantity:{$sum:"$quantity"}}}]) //you say $quantity coz you are referring to the value inside quanitity. if you dont give dollar sign then it just put a string 'quanitity'. $match is like where
```


CREATE TABLE salesman (
    salesman_id INT PRIMARY KEY,
    name VARCHAR(255),
    city VARCHAR(255),
    commission DECIMAL(4, 2)
);

INSERT INTO salesman (salesman_id, name, city, commission) VALUES
(5001, 'James Hoog', 'New York', 0.15),
(5002, 'Nail Knite', 'Paris', 0.13),
(5005, 'Pit Alex', 'London', 0.11),
(5006, 'Mc Lyon', 'Paris', 0.14),
(5003, 'Lauson Hen', NULL, 0.12),
(5007, 'Paul Adam', 'Rome', 0.13);
 
CREATE TABLE orders (
    ord_no INT PRIMARY KEY,
    purch_amt DECIMAL(10, 2),
    ord_date DATE,
    customer_id INT,
    salesman_id INT
);
INSERT INTO orders (ord_no, purch_amt, ord_date, customer_id, salesman_id) VALUES
(70001, 150.5, '2012-10-05', 3005, 5002),
(70009, 270.65, '2012-09-10', 3001, 5005),
(70002, 65.26, '2012-10-05', 3002, 5001),
(70004, 110.5, '2012-08-17', 3009, 5003),
(70007, 948.5, '2012-09-10', 3005, 5002),
(70005, 2400.6, '2012-07-27', 3007, 5001),
(70008, 5760, '2012-09-10', 3002, 5001),
(70010, 1983.43, '2012-10-10', 3004, 5006),
(70003, 2480.4, '2012-10-10', 3009, 5003),
(70012, 250.45, '2012-06-27', 3008, 5002),
(70011, 75.29, '2012-08-17', 3003, 5007),
(70013, 3045.6, '2012-04-25', 3002, 5001);

Select * from Orders
 
--1. Sub query - write a query to display all the orders from the orders table issued by the salesman 'Paul Adam'
SELECT *
FROM orders
WHERE salesman_id = (
    SELECT salesman_id
    FROM salesman
    WHERE name = 'Paul Adam'
);
 
--2. Write a query to display all the orders which values are greater than the average order value for 10th October 2012.
SELECT *
FROM orders
WHERE purch_amt > (
	SELECT AVG(purch_amt)
    FROM orders
    WHERE ord_date = '2012-10-10'
);
 
-- 3. Write a query to find all orders with order amounts which are above-average amounts for their customers.
SELECT *
FROM orders o
WHERE purch_amt > (
    SELECT AVG(purch_amt)
    FROM orders
    WHERE customer_id = o.customer_id
);
 
--4. Write a query to find all orders attributed to a salesman in New York.
SELECT *
FROM orders
WHERE salesman_id IN (SELECT salesman_id FROM salesman WHERE city = 'New York');
 
 
--ragav gave this to us to do the following queries
CREATE TABLE customer (
    customer_id INT PRIMARY KEY,
    cust_name VARCHAR(255),
    city VARCHAR(255),
    grade INT NULL,
    salesman_id INT
);

INSERT INTO customer (customer_id, cust_name, city, grade, salesman_id) VALUES
(3002, 'Nick Rimando', 'New York', 100, 5001),
(3005, 'Graham Zusi', 'California', 200, 5002),
(3001, 'Brad Guzan', 'London', NULL, 5005),
(3004, 'Fabian Johns', 'Paris', 300, 5006),
(3007, 'Brad Davis', 'New York', 200, 5001),
(3009, 'Geoff Camero', 'Berlin', 100, 5003),
(3008, 'Julian Green', 'London', 300, 5002),
(3003, 'Jozy Altidor', 'Moscow', 200, 5007);
 

-- whenever you do subqueries some things that can help is all and any
example - find all the orders where purchase amount is more than gemma purchase amount

SELECT * FROM   orders where purch_amt > All ( 

			SELECT purch_amt FROM  orders 

			where customer_id = 3005)
 
SELECT * FROM   orders where purch_amt > Any ( 

			SELECT purch_amt FROM  orders 

			where customer_id = 3005)

--5. Write a query to find the name and id of all salesmen who had more than one customer.

select * from salesmen where salesmen_id in (select salesman_id from customer group)

-- 6.  Write a query to display only those customers whose grade are, in fact, higher than every customer in New York.
SELECT * from customers where grade>ALL(select grade from customers where city='New York')

-- 7. Write a query to find all orders with an amount smaller than any amount for a customer in London.

```sql
select * from orders where purch_amt<ANY(select purch_amt from orders  JOIN salesmen ON salesmen_id=salesmen_id Join customers on salesmen_id=salesmen_id where city='London')
```

SELECT *
FROM orders
WHERE purch_amt < ANY (
    SELECT purch_amt
    FROM orders
    WHERE customer_id IN (
        SELECT customer_id
        FROM customer
        WHERE city = 'London'
    )
);

# designing database