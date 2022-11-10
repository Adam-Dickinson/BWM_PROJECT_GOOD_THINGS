from django.contrib import admin
from .models import CarCrash, CarCrashRandom
from django.contrib.auth.models import Group

admin.site.site_header = "BMW Project Administration"

class CarcrashAdmin(admin.ModelAdmin):
    list_display = ('Name', 'CarType',)
    list_filter = ('CarType',)
    
    


# Register your models here.
admin.site.register(CarCrash)
admin.site.register(CarCrashRandom)
#admin.site.unregister(Group)
