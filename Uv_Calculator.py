Python 3.13.2 (tags/v3.13.2:4f8bb39, Feb  4 2025, 15:23:48) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import requests
import json


# Function to get latitude and longitude from the city name using OpenCage API
def get_coordinates_from_city(api_key, city_name):
    """
    Fetch the latitude and longitude coordinates for a given city name.
    Uses the OpenCage API to convert city names into geographic coordinates.
    """
    url = f'https://api.opencagedata.com/geocode/v1/json?q={city_name}&key={api_key}'
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        if data['results']:
            latitude = data['results'][0]['geometry']['lat']
            longitude = data['results'][0]['geometry']['lng']
            return latitude, longitude
        else:
            print("No results found for the specified city.")
            return None, None
    except requests.exceptions.RequestException as err:
        print(f"Error occurred while fetching coordinates: {err}")
        return None, None


# Function to get UV radiation data from OpenUV API
def get_uv_radiation(api_key, latitude, longitude):
    """
    Fetch the current UV radiation index using latitude and longitude.
    Uses the OpenUV API to provide UV index details for the specified location.
    """
    url = f'https://api.openuv.io/api/v1/uv?lat={latitude}&lng={longitude}'
    headers = {'Content-Type': 'application/json', 'x-access-token': api_key}
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as err:
        print(f"Error occurred while fetching UV data: {err}")
        return None


# Function to get sunrise, sunset, and safe sun exposure time
def get_sun_times(api_key, latitude, longitude):
    """
    Fetch sunrise, sunset, and recommended sun exposure time.
    Uses the OpenUV API to provide sun exposure-related information.
    """
    url = f'https://api.openuv.io/api/v1/uv?lat={latitude}&lng={longitude}'
    headers = {'Content-Type': 'application/json', 'x-access-token': api_key}
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()
        if 'result' in data and 'sun_info' in data['result']:
            sun_times = data['result']['sun_info']['sun_times']
            safe_exposure = data['result'].get('safe_exposure_time', {})
            return sun_times, safe_exposure
        else:
            print("No sun time data available.")
            return None, None
    except requests.exceptions.RequestException as err:
        print(f"Error occurred while fetching sun time data: {err}")
        return None, None


# Function to display UV and sun time data
def display_data(uv_data, sun_time_data, safe_exposure):
    """
    Display formatted UV radiation, sunrise/sunset times, and safe sun exposure time.
    """
    print("\n================ UV & Sun Exposure Report ================\n")

    if uv_data and 'result' in uv_data:
        print("UV Radiation Information:")
        print(f"  - Current UV Index: {uv_data['result']['uv']}")
        print(
            f"  - Maximum UV Index Today: {uv_data['result']['uv_max']} (Expected at {uv_data['result']['uv_max_time']})")
    else:
        print("No UV data available.")

    if sun_time_data:
...         print("\nSunrise & Sunset Information:")
...         print(f"  - Sunrise: {sun_time_data.get('sunrise', 'N/A')}")
...         print(f"  - Sunset: {sun_time_data.get('sunset', 'N/A')}")
...     else:
...         print("No sun time data available.")
... 
...     if safe_exposure:
...         print("\nRecommended Safe Sun Exposure Times:")
...         for skin_type, time in safe_exposure.items():
...             print(f"  - {skin_type}: {time} minutes")
...     else:
...         print("No safe sun exposure data available.")
... 
...     print("\n==========================================================\n")
... 
... 
... # Function to prompt the user to input a city name
... def get_city_name():
...     """
...     Prompt user to enter a city name and return it.
...     """
...     return input("Enter the city name: ")
... 
... 
... # Example usage
... geocoding_api_key = 'api_key'  # Replace with your OpenCage API key
... uv_api_key = 'api_key'  # Replace with your OpenUV API key
... 
... # Get city name from user input
... city_name = get_city_name()
... 
... # Fetch coordinates for the entered city
... latitude, longitude = get_coordinates_from_city(geocoding_api_key, city_name)
... 
... # If valid coordinates are retrieved, fetch UV and sun time data
... if latitude is not None and longitude is not None:
...     uv_data = get_uv_radiation(uv_api_key, latitude, longitude)
...     sun_time_data, safe_exposure = get_sun_times(uv_api_key, latitude, longitude)
