from django.db import models
from django.utils import timezone


class Sensor(models.Model):
    serial_num = models.CharField(max_length=64, unique=True)
    
    def __str__(self):
        return f"{self.serial_num}"

class Heartbeat(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE)
    time_recieved = models.DateTimeField(editable=False)

    def save(self, *args, **kwargs):
        # Set timestamp on creation
        self.time_recieved = timezone.now()
        return super(Heartbeat, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.sensor}@{self.time_recieved}"