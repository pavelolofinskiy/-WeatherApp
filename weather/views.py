import requests
from django.shortcuts import render

def index(request):
    appid = '4c88cdaed527545929061dd19080c585'
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + appid

    city = 'London'
    res = requests.get(url.format(city)).json()

    city_info = {
        'city': city,
        'temp': res["main"]["temp"],
        'icon': res["weather"][0]["icon"],
    }

    context = {'info': city_info}

    return render(request, 'index.html', context)
