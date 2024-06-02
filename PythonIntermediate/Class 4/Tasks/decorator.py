import requests
import random
import functools


def get_random_swanson_quote():
    try:
        response = requests.get("https://ron-swanson-quotes.herokuapp.com/v2/quotes")
        response.raise_for_status()
        quotes = response.json()
        return random.choice(quotes)
    except Exception as e:
        print(f"Error fetching Ron Swanson quote: {e}")
        return None


def print_swanson_quote_on_run(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        quote = get_random_swanson_quote()
        if quote:
            print(f"Ron Swanson says: '{quote}'")
        return func(*args, **kwargs)

    return wrapper


# Example usage:
@print_swanson_quote_on_run
def example_function():
    print("This is the decorated function.")


example_function()
