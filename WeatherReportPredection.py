import requests
import time

# Define the API key and the base URL for OpenWeatherMap API
API_KEY = 'your_api_key_here'  # Replace with your API key from OpenWeatherMap
BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"

# Function to get weather data for a given city
def get_weather(city):
    # Construct the full API URL
    url = f"{BASE_URL}q={city}&appid={API_KEY}&units=metric"
    
    # Make the API request
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()
        
        # Extract required weather information
        main = data['main']
        weather = data['weather'][0]
        wind = data['wind']
        
        # Get current temperature, pressure, humidity
        temperature = main['temp']
        pressure = main['pressure']
        humidity = main['humidity']
        
        # Get weather description (e.g., clear sky, rain)
        weather_description = weather['description']
        
        # Get wind speed
        wind_speed = wind['speed']
        
        # Display the weather data
        print(f"Weather in {city}:")
        print(f"Temperature: {temperature}°C")
        print(f"Pressure: {pressure} hPa")
        print(f"Humidity: {humidity}%")
        print(f"Weather Description: {weather_description}")
        print(f"Wind Speed: {wind_speed} m/s")
        print("-" * 40)
    
    else:
        # If the API request failed, print an error message
        print("Error fetching data from OpenWeatherMap.")
        print("HTTP Status Code:", response.status_code)

# Main program to monitor the weather
def monitor_weather(city):
    while True:
        # Get the weather data and print it
        get_weather(city)
        
        # Wait for 10 minutes before fetching the data again
        time.sleep(600)  # 600 seconds = 10 minutes

# Replace 'London' with your city name
city = "London"
monitor_weather(city)

### Output

# Weather in London:
# Temperature: 15.2°C
# Pressure: 1012 hPa
# Humidity: 82%
# Weather Description: scattered clouds
# Wind Speed: 3.09 m/s
# ----------------------------------------
