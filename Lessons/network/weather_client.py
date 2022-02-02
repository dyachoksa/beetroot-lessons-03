import sys
import os
import pprint

import requests


def show_weather(city):
    """
    // Current Weather API Endpoint

    http://api.weatherstack.com/current?access_key=YOUR_ACCESS_KEY&query=New+York
    
    // optional parameters: 

    & units = m
    & language = en
    & callback = MY_CALLBACK
    """
    api_key = os.environ["WEATHER_API_KEY"]

    api_base_url = "http://api.weatherstack.com/current"

    params = {
        "access_key": api_key,
        "query": city
    }

    response = requests.get(api_base_url, params=params)
    data = response.json()

    print("Location:", data["request"]["query"])
    print("Current temperature: {}℃".format(data["current"]["temperature"]))
    print("Wind: {}m/s".format(data["current"]["wind_speed"]))

    print("\nFull response:")
    pprint.pprint(data)


def main():
    # python weather_client.py <City Name>
    try:
        city = sys.argv[1]
    except IndexError:
        city = "Stockholm"
    
    show_weather(city)


if __name__ == "__main__":
    main()
