import requests
import sys

city = input('Enter the city you want to check the weather for: \n')

url = f'http://api.weatherapi.com/v1/current.json?key=5b04723751fd44bca1b162545250102&q={city}&aqi=no'

try:
    # Fetches data from the specified API URL.
    response = requests.get(url)
    # Raises:
    #   Exception: If the API request fails (e.g., network error, invalid response).
    response.raise_for_status()  # Raise an exception for bad status codes (e.g., 4xx, 5xx)
    # Successfully got the data from api
    weather_json = response.json()

    temp = weather_json.get('current').get('temp_f')
    description = weather_json.get('current').get('condition').get('text')

    print(f"Today's weather in {city} is {description} with {temp} degrees.")
except requests.exceptions.RequestException as e:
    print(f"Sorry something went wrong, we couldn't get the weather report for the requested city: {city}")
    print(f"Please try again with another city.")
    # print(f"Error fetching data from API: {e}")
    sys.exit(1)  # Stop program execution
