import json

from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from channels.layers import get_channel_layer
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import (Sensor, Heartbeat)
from .views import PAGE_LIMIT


class DashboardConsumer(WebsocketConsumer):
    def websocket_connect(self, event):
        print("connected", event)
        async_to_sync(self.channel_layer.group_add)(
            'new_data', self.channel_name)
        self.accept()
        
    def websocket_disconnect(self, event):
        print("disconnected", event)
        async_to_sync(self.channel_layer.group_discard)(
            'new_data', self.channel_name)

    def websocket_receive(self, event):
        print("receive", event)

    def refresh_data(self, event):
        # Grab 25 latest sensors and heartbeats
        # Convert objects to text representations before sending
        latest_sensors = Sensor.objects.all().order_by('-id')[:PAGE_LIMIT]
        latest_sensors_text = []
        for sensor in latest_sensors:
            latest_sensors_text.append(str(sensor))
        latest_heartbeats = Heartbeat.objects.all().order_by('-id')[:PAGE_LIMIT]
        latest_heartbeats_text = []
        for heartbeat in latest_heartbeats:
            tmp = str(sensor)
            latest_heartbeats_text.append(str(heartbeat))
        # Construct and send new data on WebSocket
        json_data = json.dumps({
                'sensors': latest_sensors_text,
                'heartbeats': latest_heartbeats_text
            })
        self.send(json_data)

    @staticmethod
    @receiver(post_save)
    def my_callback(sender, **kwargs):
        # After every database save, send a signal to refresh dashboard data
        layer = get_channel_layer()
        async_to_sync(layer.group_send)(
            'new_data', {'type': 'refresh.data'})
