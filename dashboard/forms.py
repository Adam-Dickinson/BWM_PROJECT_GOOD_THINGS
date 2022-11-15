from django import forms
from .models import CarCrashRandom, FirstName, LastName, TypeOfCrash, TypeOfCar, Damage, DriverSight

class CrashForm(forms.ModelForm):
    class Meta:
        model = CarCrashRandom
        fields = ['FirstName', 'Surname', 'TypeOfCar' ,'TypeOfCrash', 'Damage', 'DriverSight' ,'FlexSensorReading', 'Speed']

class NameForm(forms.ModelForm):
    class Meta:
        model = FirstName
        fields = ['FirstName']

class SurnameForm(forms.ModelForm):
    class Meta:
        model = LastName
        fields = ['Surname']

class CarForm(forms.ModelForm):
    class Meta:
        model = TypeOfCar
        fields = ['TypeOfCar']

class TypeCrashForm(forms.ModelForm):
    class Meta:
        model = TypeOfCrash
        fields = ['TypeOfCrash']

class DamageForm(forms.ModelForm):
    class Meta:
        model = Damage
        fields = ['Damage']

class SightForm(forms.ModelForm):
    class Meta:
        model = DriverSight
        fields = ['DriverSight']