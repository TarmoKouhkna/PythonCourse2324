# Create a calculator that would ask user for
# first number, action, second number, than do the action, display the result,
# ask user if he would like to do more actions: if yes, start the program again. if no, terminate the program.

print("Welcome!")

while True:

    first_number = float(input("Insert first number: "))
    action = input("Insert action: (+, -, *, /): ")
    second_number = float(input("Insert second number: "))

    if action == "+":
        result = first_number + second_number
    elif action == "-":
        result = first_number - second_number
    elif action == "*":
        result = first_number * second_number
    elif action == "/":
        result = first_number / second_number

    print(f"Result is: {result}")

    user_input = input("Do more? (y/n):")

    if user_input == "n":
        break
