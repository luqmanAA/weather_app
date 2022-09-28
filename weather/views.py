from django.shortcuts import render
from django.views.generic import DetailView
from django.views import View

from weather_app.helpers.weatherapi import get_weather


# Create your views here.


class TodayWeatherView(DetailView):
    pass


class WeatherDetailView(View):

    def get(self, request, **kwargs):
        location = kwargs['location']
        response = get_weather(location=location)
        return render(
            request,
            'weather/detail.html',
            context=response
        )
