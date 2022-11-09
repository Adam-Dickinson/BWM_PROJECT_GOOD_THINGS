from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='dashboard-index'),
    path('staff/', views.staff, name='dashboard-staff'),
    path('crash/', views.crash, name='dashboard-crash'),
    path('order/', views.order, name='dashboard-orders'),
]