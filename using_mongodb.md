# Using MongoDB
## Basics
Install MongoDB server, shell, compass, and tools.
Ensure the mongodb server and tools bin files are added to `PATH`.

Ensure your mongodb server is running by running `mongod`.

Boot up mongo shell with `mongosh` and mongo compass.

### Creating/ Using a specific database
We can do this with the `use` command.
```
test> use sparta
switched to db sparta
sparta>
```
### Creating a collection

Now we create a collection

```
sparta> db.createCollection("academy")
< {ok: 1}
```
We can verify this in compass

### Adding entries
 We can add entries by using `insertOne` or `insertMany`
```
sparta> db.academy.insertOne({"name":"Dafydd"})
```
### Creating validation
First, let's create a new collection
```
sparta> db.creatCollection("students")
```

In compass, we can create a validation rule
![img.png](images/img.png)

and we add the code 
```
{
  $jsonSchema: {
    bsonType: 'object',
    required: [
      'name',
      'course'
    ]
  }
}
```

This makes it so all entries must have a name and course set

### Updating entries
```
sparta> db.students.insertOne({name:"Mr S. Global", year: NumberInt(2024), scor:88.2, address: {city:"Birmingham"},course:"Data"})
sparta> db.students.updateOne({name: "Mr S. Global"}, {$set: {score: 92.5, newField: true}})
```
Where the first part of the command is a filter, and the second part is what to update, changing an existing value and adding a new value

### Deleting entries
Similarly, we can delete entries with `deleteOne` or `deleteMany`, below we will delete everything by applying no filter
```
sparta> db.students.deleteMany()
< {
    acknowledge: true,
    deletedCount: 1
    }

```


## Exercises

### Exercise 1
Create a collection to store information about your favourite films. 
Add appropriate validation rules, then insert at least 3 documents. 
Practice using both .insertOne() and .insertMany(). 
You may want to type commands into a text editor then paste into the shell.

Create collection:
```
db.createCollection("films")
```
Add validation
```
{
  $jsonSchema: {
    bsonType: 'object',
    required: [
      'name',
      'year',
      'imdb_rating'
    ]
  }
}
```
insertOne
```
db.films.insertOne({name: "Robocop", year: NumberInt(1987), imdb_rating: 7.6})
db.films.insertOne({name: "The Dark Knight", year: NumberInt(2008), imdb_rating: 9.0})
```
insertMany
```
db.films.insertMany([{name: "12 Angry Men", year: NumberInt(1957), imdb_rating: 9.0}, {name: "Avengers: Infinity War", year: NumberInt(2018), imdb_rating: 8.4}, {name: "Oppenheimer", year: NumberInt(2023), imdb_rating: 8.3}])
```

### Exercise 2
Add a new document to the collection, add a new field to that document, remove that field and then remove the document entirely.

Add new document
```
db.films.insertOne({name: "Toy Story 3", year: NumberInt(2010), imdb_rating: 8.3})
```
Add new field
```
db.films.updateOne({name: "Toy Story 3"}, {$set:{genre:["Animation","Adventure","Comedy"]}})
```

Remove document entirely
```
db.films.deleteOne({name: "Toy Story 3"})
```
### Exercise 3
Install mongotools. Add the path to its bin folder to the PATH variable (will be inside MongoDB folder)
### Exercise 4
Download StarWars.zip. Extract it in a reasonable location. In the terminal (not mongosh) navigate to the folder, make sure it is the one that has all the json files. Then run the following command to add each to a new db called "starwars"
```
for i in *.json; do
    mongoimport --db starwars --collection characters --jsonArray --file "$i"
done
```
### Exercise 5
Write a query that finds the Luke Skywalker document
```
use starwars
db.characters.find({name:"Luke Skywalker"})
```

Return the value of name and eye_colour only, from the "chewbacca" document
```
db.characters.find({name:"Chewbacca"},{name: 1, eye_color: 1})
```
Find a way to check the species name of admiral ackbar, this is in an embedded document ("Species")
```
db.characters.find({name: "Ackbar"}, {species: 1})
```
### Exercise 6
Write a query that gives us only the names + homeworld names of humans in the database?
```
db.characters.find({"species.name":"Human"},{name:1,"homeworld.name":1})
```
### Exercise 7
Write a query that gives us all the entries that have an eye_colour of either "yellow" or "orange"

```
db.characters.find({$or: [{eye_colour: "yellow"}, {eye_colour: "orange"}]}) 
```

### Exercise 8
You can combine filters using $and or $or

Write a query that filter for characters that have both blue eyes and are female
```
db.characters.find({$and: [{eye_color: "blue"}, {gender: "female"}]}) 
```

Then write a query that filters for characters that have either blue eyes or are female
```
db.characters.find({$or: [{eye_colour: "blue"}, {gender: "female"}]}) 
```
### Exercise 9 
You can use comparison operators in your queries

Write a query that finds characters with a height over 200cm
```
db.characters.find({height: {$gt: "200"}})
```
Note, Height has been recorded as a string and there are some missing a height value entirely. Can you find out how to convert all the height strings to ints?
```
db.characters.aggregate([{$addFields:{height:{$toInt:"$height"}}}]) 
```
Run your initial height query again to confirm your solution works.



### Exercise 10

Experiment with the following operators. What does each do?

#### `$eq`
Checks for 
#### `$gt`
#### `$gte`
#### `$in`
#### `$lt`
#### `$lte`
#### `$ne`
#### `$nin`