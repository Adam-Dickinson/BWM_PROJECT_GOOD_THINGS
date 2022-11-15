from django.contrib import admin
from .models import CarCrash, CarCrashRandom, FirstName, LastName, TypeOfCrash, TypeOfCar, DriverSight, Damage
from django.contrib.auth.models import Group

admin.site.site_header = "BMW Project Administration"

class CarcrashAdmin(admin.ModelAdmin):
    list_display = ('Name', 'CarType',)
    list_filter = ('CarType',)
    
    


# Register your models here.
admin.site.register(CarCrash)
admin.site.register(CarCrashRandom)
admin.site.register(FirstName)
admin.site.register(LastName)
admin.site.register(TypeOfCar)
admin.site.register(TypeOfCrash)
admin.site.register(Damage)
admin.site.register(DriverSight)
#admin.site.unregister(Group)
