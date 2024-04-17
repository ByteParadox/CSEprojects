import requests
from tkinter import *
from PIL import Image, ImageTk

# Function to fetch weather data from OpenWeatherMap API
def get_weather(city):
    api_key = "78d69fcd13dfbf641bab70913a335058"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    weather_data = response.json()
    if 'weather' in weather_data:
        weather_info["text"] = f"Weather: {weather_data['weather'][0]['main']}"
        temp_info["text"] = f"Temperature: {weather_data['main']['temp']}°C"
    else:
        weather_info["text"] = "Weather data not available."

# Initialize Tkinter window
root = Tk()
root.title("Weather App")

# Add widgets
city_label = Label(root, text="Enter City:")
city_label.pack()

city_entry = Entry(root)
city_entry.pack()

submit_button = Button(root, text="Submit", command=lambda: get_weather(city_entry.get()))
submit_button.pack()

weather_info = Label(root, text="")
weather_info.pack()

temp_info = Label(root, text="")
temp_info.pack()

# Run the Tkinter event loop
root.mainloop()
