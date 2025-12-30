from django.db import models

# Create your models here.
class HealthReading(models.Model):
    # Model to store health readings such as heart rate and blood pressure
    heart_rate = models.IntegerField()
    spo2 = models.IntegerField()
    temperature = models.FloatField(null=True, blank = True)

    # Metadata 
    timestamp = models.DateTimeField(auto_now_add=True)
    device_id = models.CharField(max_length = 50, default = "ESP32_001")

    def __str__(self):
        return f"HR: {self.heart_rate}, SpO2: {self.spo2}% at {self.timestamp}"

       

