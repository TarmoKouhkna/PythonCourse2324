import pandas as pd
import json


def clean_electronics_data(json_file_path, csv_file_path):

    with open(json_file_path, 'r') as file:
        data = json.load(file)['data']

    df = pd.DataFrame(data)

    df['price'] = df['price'].astype(str).str.replace('$', '').str.replace(',', '').astype(float)

    df['stock'] = df['stock'].fillna(0).astype(int)

    df['description'] = df['description'].fillna('N/A')
    df['warranty'] = df['warranty'].fillna('N/A')

    df.to_csv(csv_file_path, index=False)
    print(f"Cleaned data saved to {csv_file_path}")


json_file_path = 'electronics_products.json'
csv_file_path = 'cleaned_electronics_products.csv'
clean_electronics_data(json_file_path, csv_file_path)
