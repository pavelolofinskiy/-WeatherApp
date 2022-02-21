import requests
from django.shortcuts import render
from .models import City

def index(request):
    appid = '4c88cdaed527545929061dd19080c585'
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + appid




    cities = City.objects.all()

    all_cities = []

    for city in cities:
        res = requests.get(url.format(city)).json()
        city_info = {
            'city': city.name,
            'temp': res["main"]["temp"],
            'icon': res["weather"][0]["icon"],
        }

        all_cities.append(city_info)

    context = {'all_info': all_cities}

    return render(request, 'index.html', context)
