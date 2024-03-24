"""
Write a program where when it starts user is given a couple of options:
[Register new user, Display users, Q for close the program]
if register new user is selected ask user some basic information:
name, age, city, amount of potatoes consumed yesterday. Append that data to users list,
print thanks to user and return to main menu asking user for his action.
if Display users is selected print the data about each user where every line would look like this:
The participant {name}, aged {age} years old, coming from {city}
have destroyed {amount_of_potatoes} potatoes yesterday.
if Q for close the program selected, close the program.
"""

users = []

while True:
    print("1. Register new user")
    print("2. Display users")
    print("Q. Close the program")

    choice = input("Choose the action: ")

    if choice == "1":
        name = input("Name: ")
        age = input("Age: ")
        city = input("City: ")
        potatoes = input("Destroyed potatoes yesterday: ")

        user = {"name": name, "age": age, "city": city, "potatoes": potatoes}
        users.append(user)

        print("Data input OK")

    elif choice == "2":
        for user in users:
            print(
                f"User {user['name']}, {user['age']} years, from {user['city']} eat {user['potatoes']} potatoes yesterday.")

    elif choice == "q":
        break

    print()
