import requests
from django.shortcuts import render
from .models import City
from .forms import CityForm
def index(request):
	url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=39133f7cf7416eb2626f02554c23e990'
	cities = City.objects.all()
	if request.method == 'POST':
		form = CityForm(request.POST)
		form.save() # will validate and save if validate

   
	form = CityForm()

	weather_data = []
	for city in cities:
		city_weather = requests.get(url.format(city)).json()
		weather ={
            'city' : city.name,
            'temperature' : city_weather['main']['temp'],
            'description' : city_weather['weather'][0]['description'],
            'icon' : city_weather['weather'][0]['icon']
        }
		weather_data.append(weather) #add the data for the current city into our list
	context = {'weather_data' : weather_data, 'form' : form}
	print(weather_data)
	
	return render(request, 'weather/weather.html',context)
# Create your views here.
