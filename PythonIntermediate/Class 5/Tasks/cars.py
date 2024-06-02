import pandas as pd
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime

# Read the cars.csv file
df = pd.read_csv('cars.csv')

# Group the cars by Make and Model and find the latest year for each group
latest_cars = df.loc[df.groupby(['car_make', 'car_model'])['car_year'].idxmax()]

# Filter out cars purchased since 2015/01/01 with no car accidents
filtered_cars = df[(df['car_purchase_date'] >= '2015-01-01') & (df['car_accidents'] == 0)]

# Identify lucky finds based on mileage and price criteria
lucky_finds = df[(df['car_mileage'] < 150000) & (df['car_price'] < 10000)]

# Find cars that meet the criteria your wife would like
wife_cars = df[(df['car_color'] == 'red') & (df['car_accidents'] == 0) & (df['car_year'] >= 2018)]

# Implement multithreading for faster execution
def process_data(data):
    # Task-specific processing or actions can be added here
    wife_cars_in_chunk = data[(data['car_color'] == 'red') & (data['car_accidents'] == 0) & (data['car_year'] >= 2018)]
    print(wife_cars_in_chunk)

# Split the data into chunks for multithreading
chunk_size = len(df) // 5
chunks = [df[i:i+chunk_size] for i in range(0, len(df), chunk_size)]

# Process the data using ThreadPoolExecutor
with ThreadPoolExecutor(max_workers=5) as executor:
    executor.map(process_data, chunks)
