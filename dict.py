# dict works almost like the real dictionary

person = {"name": "MIAL", "Age": 17, "city": "agadir" }
print(person["name"]) #will print MIAL

person["age"] = 19  # we can change a value
print(person["age"])  # prints 19

person["job"] = "student" # we can add a new value
print(person) 

if "city" in person: # we can check if a value exist
    print("City exists!")

for key, value in person.items():
    print(key, value) # print all the informations