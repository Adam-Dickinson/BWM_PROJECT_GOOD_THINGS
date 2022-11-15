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
    path('order/', views.order, name='dashboard-orders'),
    path('admin/', AdminSite, name='admin'),
]