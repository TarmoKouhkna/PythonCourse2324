import requests


def get_interesting_fact():
    # Define the URL for the Numbers API with today's date
    url = "http://numbersapi.com/{month}/{day}/date".format(month="4", day="14")  # Change the month and day as needed

    try:
        # Send a GET request to the API
        response = requests.get(url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Print the fact
            print("Interesting Fact about Today (April 14th):")
            print(response.text)
        else:
            print("Failed to fetch the data. Status code:", response.status_code)
    except Exception as e:
        print("An error occurred:", e)


if __name__ == "__main__":
    get_interesting_fact()
