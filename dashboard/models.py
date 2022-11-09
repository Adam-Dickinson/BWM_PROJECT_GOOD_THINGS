from django.db import models

# Create your models here.
AREALOOKING = (
    ('Front', 'Front'),
    ('Behind', 'Behind'),
    ('Left', 'Left'),
    ('Right', 'Right'),
)


class CarCrash(models.Model):
    name = models.CharField(max_length = 100)
    carType = models.CharField(max_length = 100)
    AreaLooking = models.CharField(max_length = 100, choices=AREALOOKING)
    FlexSensorBend = models.PositiveIntegerField()
    Speed = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.name}-{self.carType}'