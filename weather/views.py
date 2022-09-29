from datetime import datetime, timedelta
import time
from django.http import Http404
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
        if 'yesterday' in request.get_full_path():
            yesterday = datetime.today() - timedelta(days=1)
            yesterday_timestamp = yesterday.timestamp()
            response = get_weather(
                location=location,
                dt=yesterday_timestamp
            )
        else:
            response = get_weather(
                location=location,
            )
        # print(response)
        if response['cod'] == '404':
            raise Http404
        return render(
            request,
            'weather/detail.html',
            context=response
        )
