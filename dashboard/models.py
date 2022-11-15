from django.db import models

# Create your models here.

#IGNORE FROM HERE#
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
#TO HERE THIS IS TEST MODEL#

#REAL MODELs
class FirstName(models.Model):
    FirstName = models.CharField(max_length=100)
    def __str__(self):
        return f'{self.FirstName}'

class LastName(models.Model):
    Surname = models.CharField(max_length=100)
    def __str__(self):
        return f'{self.Surname}'

class TypeOfCar(models.Model):
    TypeOfCar = models.CharField(max_length=100)
    def __str__(self):
        return f'{self.TypeOfCar}'

class TypeOfCrash(models.Model):
    TypeOfCrash = models.CharField(max_length=100)
    def __str__(self):
        return f'{self.TypeOfCrash}'

class Damage(models.Model):
    Damage = models.CharField(max_length=100)
    def __str__(self):
        return f'{self.Damage}'

class DriverSight(models.Model):
    DriverSight = models.CharField(max_length=100)
    def __str__(self):
        return f'{self.DriverSight}'

class CarCrashRandom(models.Model):
    FirstName = models.ForeignKey(FirstName, on_delete=models.CASCADE)
    Surname = models.ForeignKey(LastName, on_delete=models.CASCADE)
    TypeOfCar = models.ForeignKey(TypeOfCar, on_delete=models.CASCADE)
    TypeOfCrash = models.ForeignKey(TypeOfCrash, on_delete=models.CASCADE)
    Damage = models.ForeignKey(Damage, on_delete=models.CASCADE)
    DriverSight = models.ForeignKey(DriverSight, on_delete=models.CASCADE)
    FlexSensorReading = models.PositiveIntegerField()
    Speed = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.FirstName} - {self.Surname}'



