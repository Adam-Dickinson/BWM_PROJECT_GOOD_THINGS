from django import forms
from .models import CarCrashRandom
import random

class CrashForm(forms.ModelForm):
    class Meta:
        model = CarCrashRandom
        fields = ['FirstName', 'Surname', 'TypeOfCar' ,'TypeOfCrash', 'Damage', 'DriverSight' ,'FlexSensorReading', 'Speed']

        FirstName = str(random.randrange(0,14))
        Surname = str(random.randrange(0,14))
        TypeOfCar = str(random.randrange(0,3))
        TypeOfCrash = str(random.randrange(0,8)) 
        Damage = str(random.randrange(0,9))
        DriverSight = str(random.randrange(0,3))
        SensorReading = str(random.randrange(0,9))
        Speed = str(random.randrange(0,9))

        Seed = FirstName + "." + Surname + "." + TypeOfCar + "." + TypeOfCrash + "." + Damage + "." + DriverSight + "." + SensorReading + "." + Speed
        aFirstName = ["John", "Latasha","Manual","Kevin","Guy" ,"Jayne","Werner" ,"Bridgette" ,"Richard","Olga" ,"Rayford","Lazaro" ,"Deandre", "Sam", "Ben"]
        aSurname = ["Smith","Cabrera", "Hoffman", "Zavala", "Wang Schmitt", "Rhodes", "Reilly Haney", "Holland", "Fletcher", "Shannon", "Wilson", "Hendrick", "Mtshali", "Goodman", "Dickinson"]
        aTypeOfCar = ["BMW 1-Series", "BMW X5", "BMW i3", "BMW iX"]
        aTypeOfCrash = ["Head On Collison", "T-Bone Collision", "Fender Bender Collision", "Rear-End Collision", "Burst Tire", "Paint Trade Collision", "Overturn Collision", "Pedestrian Collision", "Collision with Static Object"]
        aDamage = ["Broken Axil", "Tire Damage", "Broken Window" , "Head On Collison", "T-Bone Collision", "Fender Bender Collision", "Rear-End Collision", "Burst Tire", "Paint Trade Collision", "Overturn Collision", "Pedestrian Collision"]
        aDriverSight = ['Front', 'Right', 'Left', 'Behind']
        aSensorReading = [20, 50, 90, 180, 50, 70, 40, 100, 56, 300]
        aSpeed = ["25km/h", "40km/h", "60km/h", "80km/h", "100km/h", "120km/h", "150km/h", "200km/h", "250km/h", "300km/h"]

        dFirstName = aFirstName[int(FirstName)]
        dSurname = aSurname[int(Surname)]
        dTypeOfCar = aTypeOfCar[int(TypeOfCar)]
        dTypeOfCrash = aTypeOfCrash[int(TypeOfCrash)]
        dDamage = aDamage[int(Damage)]
        dDriverSight = aDriverSight[int(DriverSight)]
        dSensorReading = aSensorReading[int(SensorReading)]
        dSpeed = aSpeed[int(Speed)]