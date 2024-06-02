import requests
import random


# Function to fetch quotes from the API
def fetch_quotes(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print("Failed to fetch quotes. Status code:", response.status_code)
        return []


# Function to sort quotes by length
def sort_quotes_by_length(quotes):
    return sorted(quotes, key=len)


# Function to save sorted quotes to a file
def save_quotes_to_file(quotes, filename):
    with open(filename, 'w') as file:
        for quote in quotes:
            file.write(quote + '\n')


# Main function
def main():
    api_url = "https://ron-swanson-quotes.herokuapp.com/v2/quotes/50"
    quotes = fetch_quotes(api_url)
    if quotes:
        sorted_quotes = sort_quotes_by_length(quotes)
        save_quotes_to_file(sorted_quotes, 'sorted_quotes.txt')
        random_quote = random.choice(sorted_quotes)
        print("Random quote:", random_quote)


if __name__ == "__main__":
    main()
