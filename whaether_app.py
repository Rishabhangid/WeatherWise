import requests
import pyttsx3

engine = pyttsx3.init()
city = input("Enter the City Name: ")
url = f"http://api.weatherapi.com/v1/current.json?key=640e15b885074ae1a95144033241511&q={city}"
r = requests.get(url)

# Parse the JSON response
data = r.json()  # Converts the response to a dictionary
temp_c = data["current"]["temp_c"]  # Access the 'temp_c' field
wind_speed = data["current"][ "wind_kph"]  # Access the 'temp_c' field

speak = f"The current temperature in {city} is {temp_c} degrees Celsius, with a wind speed of {wind_speed} kilometers per hour."

# Display the temperature
print(f"The current temperature in {city} is {temp_c}°C, Wind Speed is {wind_speed}kph.")
engine.say(speak)
engine.runAndWait()
