cars = ["VW", "Audi", "BMW"]

# Adding values to the list
cars.append("Zap")
cars.append("Jeep")
# Joining lists
cars.extend(["Nissan", "Volvo", "Opel", "VW"])
# Length of the cars list
print(f"Cars in the list {len(cars)}")
# Sort the list
cars.sort()
# Count of the certain cars
print(f'Amount of the Volkswagen cars: {cars.count("VW")}')
# Get the index of certain records
index_of_Jeep = cars.index("Jeep")
print(f"The index of Jeep in this list is: {index_of_Jeep}")
# Inserting at the certain index
cars.insert(index_of_Jeep, "Opel")
print(cars)
# Remove the item from the list at the index
cars.pop(index_of_Jeep)
# Remove the last item from the list
cars.pop()
# Reverse the list
cars.reverse()
# Clear the list
cars.clear()



