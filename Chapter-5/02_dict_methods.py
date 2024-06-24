d = {} #to create an empty dictionary

marks = {
    "Anuj":100,
    "Rahul":90,
    "Rohit":80,
    "Rohan": 76,
    "Rajeev": 45,
    "Dhruv":85
}

# print(marks.items())
# print(marks.keys())
# print(marks.values())

# marks.update({"Anuj":99, "Shubham":59}) #It will update any value of key and also can add new key and value
# print(marks)

# print(marks.get("Anuj1")) #difference between .get and the line below is that .get prints None if the key is not found 
# print(marks["Anuj1"]) #prints error

# marks.pop("Rahul") #Remove the selected key
marks.popitem() # remove the last key value pair

marks.clear() # Removes all items from the dictionary
print(marks)