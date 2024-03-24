# Write a Python program to convert a month name to a number of days.

month_name = input("Input the name of Month: ")
if month_name == "February":
    print("28 or 29 days")
elif month_name in ("April", "June", "September", "November"):
    print("30 days")
elif month_name in ("January", "March", "May", "July", "August", "October", "December"):
    print("31 days")
