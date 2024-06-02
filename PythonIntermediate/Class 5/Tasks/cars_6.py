import pandas as pd

# Read the CSV file into a pandas DataFrame
df = pd.read_csv("cars.csv")

# Convert car_purchase_date to datetime format
df['car_purchase_date'] = pd.to_datetime(df['car_purchase_date'])

# Create buckets for each task
buckets = {
    "Latest Cars": [],
    "Accident-Free Since 2015": [],
    "Lucky Finds": [],
    "Wife's Preferences": []
}

# Task 1: Find the latest cars for each Make+Model
latest_cars = df.loc[df.groupby(['car_make', 'car_model'])['car_year'].idxmax()]
buckets["Latest Cars"] = latest_cars.values.tolist()

# Task 2: Filter cars purchased since 2015/01/01 with no accidents
accident_free_since_2015 = df[(df['car_purchase_date'] >= '2015-01-01') & (df['car_accidents'] == 0)]
buckets["Accident-Free Since 2015"] = accident_free_since_2015.values.tolist()

# Task 3: Find lucky finds
lucky_finds = df[(df['car_mileage'] < 150000) & (df['car_price'] < 10000)]
buckets["Lucky Finds"] = lucky_finds.values.tolist()

# Task 4: Find cars that meet wife's preferences
wife_preferences = df[(df['car_color'] == 'red') & (df['car_accidents'] == 0) & (df['car_year'] >= 2018)]
buckets["Wife's Preferences"] = wife_preferences.values.tolist()

# Print the results
for task, bucket in buckets.items():
    print(f"\n{task}:")
    if not bucket:
        print("No cars found.")
    else:
        for i, car in enumerate(bucket[:5]):  # Print up to 5 cars per task
            print(f"  Car {i+1}:")
            for attribute, value in zip(df.columns[1:], car[1:]):  # Exclude the first column (car_make)
                print(f"    {attribute}: {value}")
