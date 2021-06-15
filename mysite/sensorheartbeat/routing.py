from django.urls import path

from .consumers import DashboardConsumer


ws_urlpatterns = [
    path('ws/dashboard/', DashboardConsumer.as_asgi())
]