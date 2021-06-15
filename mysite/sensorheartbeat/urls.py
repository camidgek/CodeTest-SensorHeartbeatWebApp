from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('sensors/', csrf_exempt(views.SensorListView.as_view()), name='sensors'),
    path('heartbeats/', csrf_exempt(views.HeartbeatListView.as_view()), name='heartbeats'),
]