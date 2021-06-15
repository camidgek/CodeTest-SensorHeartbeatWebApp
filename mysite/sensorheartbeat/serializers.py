from rest_framework import serializers

from .models import (Sensor, Heartbeat)


class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = ['id', 'serial_num']

class HeartbeatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Heartbeat
        fields = ['id', 'sensor']
