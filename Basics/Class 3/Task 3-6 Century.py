"""
The first century spans from the year 1 up to and including the year 100,
the second century - from the year 101 up to and including the year 200, etc.
Task Given a year, print the century it is in.
The year would be passed by user input
"""

year = int(input("Insert a year number: "))

century = year // 100 + 1

print(f"Year {year} is from {century} century")

