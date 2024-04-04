

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


