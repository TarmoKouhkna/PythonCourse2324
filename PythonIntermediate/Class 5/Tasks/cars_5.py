import pandas as pd
from concurrent.futures import ThreadPoolExecutor

# Read the cars.csv file
data = pd.read_csv('/Users/tarmokouhkna/PycharmProjects/PythonEE23/PythonIntermediate/Class 5/Tasks/cars.csv')

# Create a function to filter cars
def filter_cars(criteria):
    return criteria(data)

# Define the filtering criteria for each task
tasks = {
    "Latest Cars": (lambda x: x.loc[x.groupby(['car_make', 'car_model'])['car_year'].idxmax()]),
    "Recent Cars": (lambda x: x[(x['car_purchase_date'] >= '2015-01-01') & (x['car_accidents'] == 0)]),
    "Lucky Finds": (lambda x: x[(x['car_mileage'] < 150000) & (x['car_price'] < 10000)]),
    "Wife Preferences": (lambda x: x[(x['car_color'] == 'red') & (x['car_accidents'] == 0) & (x['car_year'] >= 2018)])
}

# Use ThreadPoolExecutor for multithreading
with ThreadPoolExecutor() as executor:
    results = {task: executor.submit(filter_cars, criteria) for task, criteria in tasks.items()}

# Print the results
for task, result in results.items():
    print(f"{task}:")
    print(result.result())
    print()
    