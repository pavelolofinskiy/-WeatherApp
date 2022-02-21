import requests
from django.shortcuts import render

def index(request):
    appid = '4c88cdaed527545929061dd19080c585'
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid=' + appid

    city = 'London'
    res = requests.get(url.format(city))
    print(res.text)
    return render(request, 'index.html')
