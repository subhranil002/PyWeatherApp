import requests
import json
import pyttsx3


def weatherForecast(place, apikey="0047b50c15f84212b35144033230209"):
    url = f"https://api.weatherapi.com/v1/current.json?key={apikey}&q={place}"

    r = requests.get(url)
    weather = json.loads(r.text)

    print(f"The current weather in {place} is {weather['current']['temp_c']} degree celcius, the wind speed is {weather['current']['wind_kph']} kilometer per hour, humidity is {weather['current']['humidity']}% and the condition is {weather['current']['condition']['text']}")

    return f"The current weather in {place} is {weather['current']['temp_c']} degree celcius, the wind speed is {weather['current']['wind_kph']} kilometer per hour, humidity is {weather['current']['humidity']}% and the condition is {weather['current']['condition']['text']}"


def text_to_speech(message):
    # For Windows Users
    engine = pyttsx3.init()
    engine.say(message)
    engine.runAndWait()


text_to_speech("Wellcome to, Weather App!")
text_to_speech("Enter the name of the place")
place = input("Enter the name place : ")
text_to_speech(weatherForecast(place))

