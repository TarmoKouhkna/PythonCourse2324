# Write a program that will correctly display the sentence "Alice has x cats"
# depending on the number of cats, it can show: Alice has 1 cat, Alice has 2 cats, Alice has 10 cats.
# use user input to get amount of cats.
# ** After number 20 entered, the output should be "Alice has a cat shelter"

cats = int(input("Alice has how many cats "))

if cats == 1:
    print("Alice has 1 cat.")
elif cats == 2 or cats == 3 or cats == 4:
    print(f"Alice has {cats} cats.")
else:
    print(f"Alice has {cats} cats.")

if cats >= 20:
    print("Alice has a cat shelter.")
else:
    print(f"Someone stole {cats * -1} cats")
