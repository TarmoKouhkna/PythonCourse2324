import pandas as pd

# Read the cars.csv file
data = pd.read_csv('cars.csv')

# Create four buckets of data
buckets = {}

# Group by Make and Model to find the latest year for each
latest_cars = data.loc[data.groupby(['car_make', 'car_model'])['car_year'].idxmax()]

# Filter cars purchased since 2015.01.01 with no accidents
recent_cars = data[(data['car_purchase_date'] >= '2015-01-01') & (data['car_accidents'] == 0)]

# Find lucky finds
lucky_finds = data[(data['car_mileage'] < 150000) & (data['car_price'] < 10000)]

# Find cars your wife would like
wife_preferences = data[(data['car_color'] == 'red') & (data['car_accidents'] == 0) & (data['car_year'] >= 2018)]

# Print the results
print("Latest Cars for each Make and Model:")
print(latest_cars)

print("\nCars purchased since 2015.01.01 with no accidents:")
print(recent_cars)

print("\nLucky Finds (Mileage < 150,000 and Price < $10,000):")
print(lucky_finds)

print("\nCars that your wife would like (Red, No accidents, Year 2018 or newer):")
print(wife_preferences)
