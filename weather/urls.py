from django.urls import path

from weather.views import (
    TodayWeatherView,
    WeatherDetailView
)

app_name = 'weather'

urlpatterns = [
    path('<str:location>', WeatherDetailView.as_view(), name='weather_detail'),
    path('<str:location>/<str:str>', WeatherDetailView.as_view(), name='daily_detail'),
]
