from django.urls import path

from weather.views import (
    TodayWeatherView
)

app_name = 'weather'

urlpatterns = [
    path('', TodayWeatherView.as_view, name='today'),
]
