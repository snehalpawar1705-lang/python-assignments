my_dict = {"name": "Alia", "age": 24, "city": "London"}
print("Created Dictionary:", my_dict)


# Accessing elements
print("Access 'name':", my_dict["name"])  
print("Access 'age':", my_dict.get("age"))

my_dict["age"] = 27
print("Updated 'age' to 26:", my_dict)


removed_value = my_dict.pop("city")  
print(f"Removed 'city': {removed_value}")
print("Dictionary After Removing 'city':", my_dict)


dict1 = {"a": 1, "b": 2, "c": 3}
dict2 = {"d": 4, "e": 5}
print("Dictionary 1:", dict1)
print("Dictionary 2:", dict2)

merged_dict = dict1.copy()  
merged_dict.update(dict2)  
print("Merged Dictionary:", merged_dict)
