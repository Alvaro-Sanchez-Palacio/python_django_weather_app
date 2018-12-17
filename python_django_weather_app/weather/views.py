import requests
from django.shortcuts import render


# Create your views here.
def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=bbb1e42692665ec3830fdb2d5dfe0168'
    city = 'Paris'

    response = requests.get(url.format(city)).json()

    city_weather = {
        'city': city,
        'temperature': response['main']['temp'],
        'description': response['weather'][0]['description'],
        'icon': response['weather'][0]['icon'],
    }

    print(response)
    # print(city_weather)

    context = {
        'city_weather': city_weather,
    }

    return render(request, 'weather/weather.html', context)

