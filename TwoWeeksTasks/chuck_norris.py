import requests


def get_random_chuck_norris_quote():
    url = "https://api.chucknorris.io/jokes/random"
    response = requests.get(url)
    data = response.json()
    if response.status_code == 200:
        return data['value']
    else:
        return "Failed to fetch Chuck Norris quote"


def main():
    chuck_norris_quote = get_random_chuck_norris_quote()
    print("Chuck Norris Quote:")
    print(chuck_norris_quote)


if __name__ == "__main__":
    main()
