# Create a list with 5 names in it.
# Append one name,
# insert one name at the start of the list,
# sort and reverse the list.
# Print out the indexes of these added names.

list = ["Nose", "Ear", "Eyebrows", "Hair", "Lips"]
print(list)
list.append("Chin")
print(list)

index_of_Nose = list.index("Nose")
list.insert(index_of_Nose, "Forehead")
print(list)

index_of_Chin = list.index("Chin")
print(f"The index of Chin in this list is: {index_of_Chin}")

index_of_Forehead = list.index("Forehead")
print(f"The index of Forehead in this list is: {index_of_Forehead}")

list.sort()
print(list)

list.reverse()
print(list)


