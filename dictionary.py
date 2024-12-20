personalData = {
    "name": "Khalid Ehab",
    "age": 20,
    "city": "Sadat",
    "country": "Egypt"
}

# a.	Print your name
print("Name:", personalData["name"])

# b.	Update your age
personalData["age"] = 21

# c.	Print all the dictionary items
print("\nAll Items:")
for key, value in personalData.items():
    print(f"{key}: {value}")

# d.	Print the dictionary keys
print("\n\nKeys:")
for key in personalData.keys():
    print(key)

# e.	Print the dictionary values
print("\n\nValues:")
for value in personalData.values():
    print(value)