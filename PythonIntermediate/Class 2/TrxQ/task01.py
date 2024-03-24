import json


# Function to calculate the average of a list and return integer result
def calculate_average(lst):
    if len(lst) == 0:
        return 0
    return int(sum(lst) / len(lst))


# Load data from JSON file
with open('data.json') as f:
    data = json.load(f)

# Calculate average of right side numbers
right_side_avg = calculate_average(data['right_side'])

# Calculate average of left side numbers
left_side_avg = calculate_average(data['left_side'])

# Calculate the average of both side averages
both_sides_avg = (right_side_avg + left_side_avg) // 2

# Print results
print("rightside:", right_side_avg)
print("leftside:", left_side_avg)
print("bothsides:", both_sides_avg)
