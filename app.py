import requests
from bs4 import BeautifulSoup

def get_weather(city):
    url = f"http://wttr.in/{city}?format=3" 
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.text  
    else:
        return "Не вдалося отримати погоду."

city = input("Введіть місто для перевірки погоди: ")

weather = get_weather(city)
print(f"Погода в місті {city}: {weather}")
