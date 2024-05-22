from django.db import models

# Create your models here.
class FanSpecification(models.Model):
    speed_level = models.IntegerField(primary_key=True)
    current = models.FloatField()

    def __str__(self):
        return f"Speed {self.speed_level}: {self.current} amps"

class FanEvent(models.Model):
    event_time = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField()
    speed_level = models.ForeignKey(FanSpecification, on_delete=models.CASCADE)

    def __str__(self):
        return f"Event at {self.event_time} - Status: {self.status}, Speed: {self.speed_level.speed_level}"
