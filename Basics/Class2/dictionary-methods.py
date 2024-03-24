import json

sample_dict = {
    "name": "Tarmo",
    "age": 57,
    "city": "New York",
    "dogs": ["Johnny", "Maru"],
    "family": [
    {
        "name": "Liisi",
        "age": 36
    },
{
    "name": "Anna",
    "age": 30
}
],
"married": True

}

sample_dict["favourite color"] = "Green"
sample_dict["age"] += 1
sample_dict["dogs"].append("New")

print(sample_dict)

# Get specific data from dictonary
print(sample_dict['family'])
print(sample_dict.get('city'))
print(sample_dict.get('food', 'Default value'))

# Deleting values from dictionary
del sample_dict['favourite color']
deleted_value = sample_dict.pop("family")
print(deleted_value)

print(json.dumps(sample_dict, indent=4))


