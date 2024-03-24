# Write a program to based on current time of day would return a word Morning, Day, Evening or Night.

current_time = input("Input the time: ")

if current_time in ("5", "6", "7", "8", "9", "10"):
    print("Morning")
elif current_time in ("11", "12", "13", "14"):
    print("Day")
elif current_time in ("15", "16", "17", "18"):
    print("Afternoon")
elif current_time in ("19", "20", "21", "22", "23"):
    print("Evening")
elif current_time in ("24", "1", "2", "3", "4"):
    print("Night")
