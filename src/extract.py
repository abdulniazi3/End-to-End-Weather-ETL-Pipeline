import requests
import os
from dotenv import load_dotenv


load_dotenv()

API_KEY = os.getenv("API_KEY")


def get_weather():

    url = f"https://api.openweathermap.org/data/2.5/weather?q=London&appid={API_KEY}&units=metric"


    response = requests.get(url)

    return response.json()



data = get_weather()

print(data)