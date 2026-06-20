# # A dictionary is a collection of key-value pairs. Each key is unique and maps to a value.
# a =dict(name="Rafi", age=20)
# a["name"] = "Reshma"
# a["gender"] = "Female"

# #popitem() removes the last item from the dictionary and returns it as a tuple (key, value).
# pop1 = a.popitem()
# print(a)
# print(pop1)
# #pop() removes the specified key and returns the corresponding value. If the key is not found, it raises a KeyError.
# pop2 = a.pop("age")
# print(a)
# #nested dictionary
# student = {
#     "name": "Rafi",
#     "age": 21,
#     "subjects": {
#         "math": 85,
#         "science": 90
#     },
#     "gender": "Male"
# }
# print(student["subjects"]["math"])
# #from keys() method creates a new dictionary with keys from the given iterable and values set to the specified value.
# college=dict.fromkeys(["name", "location", "established"],0)
# print(college)

# #get() method returns the value for the specified key if it exists in the dictionary.
# #  If the key is not found, it returns None or a default value if provided.
# print(student.get("name") )
#  # Returns the value for the key "name"
#  #values
# print(student.values())
# #del() statement removes the specified key-value pair from the dictionary.
# del student["gender"]
# print(student)  
# new_student={
#     "name": "Reshma",
#     "age": 20,
#  }
# new=student.update(new_student)
# print(new)

student={
    "name": "Rafi",
    "age": 21,
    "subjects": {
        "math": 85,
        "science": 90
    },
}
updated_student={
    "gender": "Male"
}