import pymongo

# Connecting to MongoDB
client = pymongo.MongoClient()
db = client["starwars"]

# ##
# luke = db.characters.find_one({"name": "Luke Skywalker"})
# # print(luke)
#
# # Getting only certain fields
# luke_short = db.characters.find_one({"name": "Luke Skywalker"}, {"name": 1, "eye_color": 1, "_id": 0})
# # print(luke_short)
#
# # Iterating through multiple records/documents
# droids = db.characters.find({"species.name": "Droid"})
#
# for d in droids:
#     print(d["name"])

# Exercise 1 - Find the height of Darth Vader, only return results for the name and the height.
print("\n\nExercise 1 ---------------\n")
darth_vader = db.characters.find_one({"name": "Darth Vader"}, {"name": 1, "height": 1, "_id": 0})
#print(darth_vader)
print(f"{darth_vader["name"]} has a height of {darth_vader["height"]}cm")

# Exercise 2 - Find all characters with yellow eyes, only return results for the names of the characters.
print("\n\nExercise 2 ---------------\n")
yellow_eyes = db.characters.find({"eye_color": "yellow"}, {"name": 1, "_id": 0})
for character in yellow_eyes:
    print(f"{character["name"]} has yellow eyes")

# Exercise 3 - Find male characters. Limit your results to only show the first 3.
print("\n\nExercise 3 ---------------\n")
males = db.characters.find({"gender": "male"}).limit(3)
for character in males:
    print(character["name"])

# Exercise 4 -Find the names of all the humans whose homeworld is Alderaan.
print("\n\nExercise 4 ---------------\n")
humans_of_alderaan = db.characters.find({"species.name": "Human", "homeworld.name": "Alderaan"}, {"_id": 0, "name": 1, "species.name": 1, "homeworld.name": 1})
for character in humans_of_alderaan:
    print(f"{character["name"]} is a {character["species"]["name"]} from {character["homeworld"]["name"]}")


# Exercise 5 - What is the average height of female characters?
print("\n\nExercise 5 ---------------\n")
female_average_height = db.characters.aggregate([{"$match": {"gender": {"$eq": "female"}}}, {"$group": {"_id": "$gender", "avgMass": {"$avg": "$mass"}}}])
for item in female_average_height:
    print(f"The average height of {item['_id']} characters is {item['avgMass']}kg")
# Exercise 6 - Which character is the tallest?
print("\n\nExercise 6 ---------------\n")
tallest = db.characters.aggregate([{"$sort": {"height": -1}}, {"$limit": 1}])
for character in tallest:
    print(f"{character['name']} is the tallest at {character['height']}cm")