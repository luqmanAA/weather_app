import json
import os
import requests

from django.conf import settings


def get_weather(location=None, lat=None, long=None, dt=None):
    api_key = '97bb0b20b9177fdaa8bfe19946a588b1'
    if lat and long:
        url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={long}&appid={api_key}&units=metric"
    else:
        if location and dt:
            url = f"https://api.openweathermap.org/data/2.5/weather?q={location}&dt={dt}&appid={api_key}&units=metric"
        else:
            url = f"https://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric"
    response = requests.get(url)
    return json.loads(response.text)

