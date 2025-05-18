import requests
from datetime import datetime

API_KEY="291c90685e9169962b82dc7ca736c266"
BASE_URL="https://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    params={
        "q": city,
        "appid": API_KEY,
        "units": "metric"
        }

    response = requests.get(BASE_URL, params=params)

    if response.status_code ==200:
        data=response.json()
        lat = data["coord"]["lat"]
        lon = data["coord"]["lon"]
        weather=data["weather"][0]["description"]
        visib=data["main"]["visibility"]
        temp=data["main"]["temp"]
        feels_like=data["main"]["feels_like"]

        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        output=(
            f"\n City: {city}"
            f"\n Coordinates: Latitiue {lat},Longitude {lon}"
            f"\n Time: {now}"
            f"\n Weather: {weather}"
            f"\n Visibility: {visib}"
            f"\n Temperature:{temp}C (feels like {feels_like}C)\n"
        )
        print(output)

        with open("weather_log.txt", "a") as file:
            file.write(output+"\n")

    else:
        print("City not found or error in the API request.")

while True:
    city_input = input("Enter city name(or type 'exit') to quit: ")
    
    if city_input.lower()=="exit":
        print("Exiting Weather App.")
        break
    
    get_weather(city_input)




