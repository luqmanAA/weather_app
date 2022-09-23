from django.urls import path

from notifications.views import (
    NotificationListView
)

app_name = 'weather'

urlpatterns = [
    path('', NotificationListView.as_view(), name='notifications'),
]
