from django import forms
from .models import CarCrashRandom

class CrashForm(forms.ModelForm):
    class Meta:
        model = CarCrashRandom
        fields = ['FirstName', 'Surname', 'TypeOfCar' ,'TypeOfCrash', 'Damage', 'DriverSight' ,'FlexSensorReading', 'Speed']