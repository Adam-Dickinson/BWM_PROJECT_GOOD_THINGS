from django.contrib import admin
from .models import CarCrash
from django.contrib.auth.models import Group

admin.site.site_header = "BMW Project Administration"

class CarcrashAdmin(admin.ModelAdmin):
    list_display = ('Name', 'CarType',)
    list_filter = ('CarType',)
    
    


# Register your models here.
admin.site.register(CarCrash)
#admin.site.unregister(Group)
