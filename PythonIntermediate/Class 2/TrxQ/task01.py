import json


# Function to calculate the average of a list and return rounded result
def calculate_average(lst):
    # Optional condition
    # if len(lst) == 0:
    #     return 0
    return round(sum(lst) / len(lst))


# Load data from JSON file
with open('data.json') as file:
    data = json.load(file)

# Calculate average of right side numbers
right_side_avg = calculate_average(data['right_side'])

# Calculate average of left side numbers
left_side_avg = calculate_average(data['left_side'])

# Calculate the average of both side averages
both_sides_avg = (right_side_avg + left_side_avg) // 2

# Print results
print("Right side average is:", right_side_avg)
print("Left side average is:", left_side_avg)
print("Average of averages is:", both_sides_avg)
