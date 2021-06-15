from django.apps import AppConfig


class SensorheartbeatConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'sensorheartbeat'

    # Enable signals
    def ready(self):
        import sensorheartbeat.consumers
