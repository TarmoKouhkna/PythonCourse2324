import pandas as pd
from concurrent.futures import ThreadPoolExecutor

# Read the cars.csv file
df = pd.read_csv('cars.csv')

# Initialize empty lists to collect results from each chunk
latest_cars_results = []
filtered_since_2015_no_accidents_results = []
lucky_finds_results = []
wife_cars_results = []

# Implement multithreading for faster execution
def process_data(chunk):
    latest_cars_chunk = chunk.loc[chunk.groupby(['car_make', 'car_model'])['car_year'].idxmax()]
    filtered_since_2015_no_accidents_chunk = chunk[(chunk['car_purchase_date'] >= '2015-01-01') & (chunk['car_accidents'] == 0)]
    lucky_finds_chunk = chunk[(chunk['car_mileage'] < 150000) & (chunk['car_price'] < 10000)]
    wife_cars_chunk = chunk[(chunk['car_color'] == 'red') & (chunk['car_accidents'] == 0) & (chunk['car_year'] >= 2018)]

    # Append results to respective lists
    latest_cars_results.append(latest_cars_chunk)
    filtered_since_2015_no_accidents_results.append(filtered_since_2015_no_accidents_chunk)
    lucky_finds_results.append(lucky_finds_chunk)
    wife_cars_results.append(wife_cars_chunk)

# Split the data into chunks for multithreading
chunk_size = len(df) // 5
chunks = [df[i:i + chunk_size] for i in range(0, len(df), chunk_size)]

# Process the data using ThreadPoolExecutor
with ThreadPoolExecutor(max_workers=5) as executor:
    executor.map(process_data, chunks)

# Concatenate results from all chunks
latest_cars = pd.concat(latest_cars_results)
filtered_since_2015_no_accidents = pd.concat(filtered_since_2015_no_accidents_results)
lucky_finds = pd.concat(lucky_finds_results)
wife_cars = pd.concat(wife_cars_results)

# Print the concatenated results
print("Latest cars for each make and model:")
print(latest_cars)
print("\nCars purchased since 2015/01/01 with no accidents:")
print(filtered_since_2015_no_accidents)
print("\nLucky finds:")
print(lucky_finds)
print("\nCars that your wife would like:")
print(wife_cars)
