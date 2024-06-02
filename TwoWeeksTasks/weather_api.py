import requests


def get_weather_forecast(api_key, latitude, longitude):
    url = f"https://api.open-meteo.com/weather?latitude={latitude}&longitude={longitude}"
    headers = {"Authorization": f"Bearer {api_key}"}
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an exception for bad status codes
        data = response.json()
        forecast = data["hourly"]
        return forecast
    except requests.exceptions.RequestException as e:
        print(f"Failed to retrieve weather forecast: {e}")
        return None
    except KeyError:
        print("No forecast data available.")
        return None


def main():
    # Replace 'YOUR_API_KEY' with your actual API key
    api_key = "YOUR_API_KEY"
    latitude = "59.319205"  # Example latitude, replace with your actual latitude
    longitude = "24.951557"  # Example longitude, replace with your actual longitude

    forecast = get_weather_forecast(api_key, latitude, longitude)

    if forecast:
        print("Weather forecast for the next 7 days:")
        for day in forecast[:7]:
            print(f"Date: {day['time']}, Temperature: {day.get('temperature_2m', 'N/A')}°C")
    else:
        print("No forecast data available.")


if __name__ == "__main__":
    main()
