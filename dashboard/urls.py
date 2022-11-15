from django.urls import path
from . import views
from django.contrib.admin import AdminSite

urlpatterns = [
    path('dashboard/', views.index, name='dashboard-index'),
    path('staff/', views.staff, name='dashboard-staff'),
    path('staff/detail/<int:pk>', views.staff_detail, name='dashboard-staff-detail'),
    path('crash/', views.crash, name='dashboard-crash'),
    path('crash/delete/<int:pk>/', views.Crash_Delete, name='dashboard-crash-delete'),
    path('crash/update/<int:pk>/', views.Crash_Update, name='dashboard-crash-update'),
    path('data/', views.crash_data, name='dashboard-crash-sim-data'),
    path('admin/', AdminSite, name='admin'),
    path('data/name', views.name_data, name='dashboard-data-name'),
    path('data/surname', views.surname_data, name='dashboard-data-surname'),
    path('data/crashtype', views.crashtype_data, name='dashboard-data-crashtype'),
    path('data/car', views.car_data, name='dashboard-data-car'),
    path('data/damage', views.damage_data, name='dashboard-data-damage'),
    path('data/sight', views.sight_data, name='dashboard-data-sight'),
]