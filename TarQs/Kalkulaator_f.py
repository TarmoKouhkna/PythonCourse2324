def calculator():
    print("Tere!")

    while True:
        first_number = float(input("Sisesta esimene number: "))
        action = input("Sisesta tehe: (+, -, *, /): ")
        second_number = float(input("Sisesta teine number: "))

        if action == "+":
            result = first_number + second_number
        elif action == "-":
            result = first_number - second_number
        elif action == "*":
            result = first_number * second_number
        elif action == "/":
            result = first_number / second_number

        print(f"Tulemus on: {result}")

        user_input = input("Kas arvutame veel? (j/e):")

        if user_input == "e":
            break
# Call the function to execute the calculator
calculator()
