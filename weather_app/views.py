import json

from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, reverse
from django.views import View

from .helpers.weatherapi import get_weather

class IndexView(View):

    def get(self, request, **kwargs):
        if request.GET.get('location'):
            query = request.GET.get('location')
            return HttpResponseRedirect(
                reverse('weather:weather_detail', args=[query])
            )
        template_name = 'index.html'
        context = {
            'index': 'Welcome to the homepage'
        }
        return render(
            request,
            template_name,
            context
        )


def weather_query_view(request, **kwargs):
    location_info = json.load(request)
    print(location_info)
    lat = location_info['lat']
    long = location_info['long']
    response = get_weather(lat=lat, long=long)
    return JsonResponse(response)


