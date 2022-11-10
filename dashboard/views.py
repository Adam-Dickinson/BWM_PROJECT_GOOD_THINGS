from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import CarCrashRandom
from .forms import CrashForm

# Create your views here.

def index(request):
    carcrashrandom = CarCrashRandom.objects.all()

    context = {
        'crash': carcrashrandom
    }

    return render(request, 'dashboard/index.html')

def staff(request):
    return render(request, 'dashboard/staff.html')

def crash(request):
    items = CarCrashRandom.objects.all()

    #items = CarCrashRandom.objects.raw('SELECT * FROM dashboard_carcrashrandom')

    if request.method == 'POST':
        form = CrashForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard-crash')
    else:
        form = CrashForm()
    context={
        'items' : items,
        'form' : form,
    }
    return render(request, 'dashboard/crash.html', context)

def order(request):
    return render(request, 'dashboard/orders.html')