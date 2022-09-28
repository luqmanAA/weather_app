from django.urls import path

from weather.views import (
    TodayWeatherView,
    WeatherDetailView
)

app_name = 'weather'

urlpatterns = [
    path('', TodayWeatherView.as_view(), name='today'),
    path('<str:location>', WeatherDetailView.as_view(), name='weather_detail')
]
