from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import CarCrashRandom, FirstName, LastName, TypeOfCrash, TypeOfCar, Damage, DriverSight
from .forms import CrashForm, CarForm, NameForm, SurnameForm, SightForm, DamageForm, TypeCrashForm
from django.contrib.auth.models import User

# Create your views here.
#Admin Views
@login_required
def index(request):
    return render(request, 'dashboard/index.html')

@login_required
def staff(request):
    users = User.objects.all()
    context={
        'users' : users,
    }
    return render(request, 'dashboard/staff.html', context)
@login_required
def staff_detail(request, pk):
    user = User.objects.get(id=pk)
    context = {
        'user' : user
    }
    return render(request, 'dashboard/staff_detail.html', context)

@login_required
def crash(request):
    items = CarCrashRandom.objects.all()

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

@login_required
def Crash_Delete(request, pk):
    item = CarCrashRandom.objects.get(id = pk)
    if request.method == 'POST':
        item.delete()
        return redirect('dashboard-crash')
    return render(request, 'dashboard/crash_delete.html')

@login_required
def Crash_Update(request, pk):
    item = CarCrashRandom.objects.get(id=pk)
    if request.method == 'POST':
        form = CrashForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('dashboard-crash')
    else:
        form = CrashForm(instance=item)
    context={
        'form' : form,
    }
    return render(request, 'dashboard/crash_update.html', context)


@login_required
def crash_data(request):
    return render(request, 'dashboard/crash_sim_data.html')

@login_required
def name_data(request):
    items = FirstName.objects.all()
    context = {
        'items' : items,
    }
    return render(request, 'dashboard/name.html',context)

@login_required
def surname_data(request):
    items = LastName.objects.all()
    context = {
        'items' : items,
    }
    return render(request, 'dashboard/surname.html',context)

@login_required
def car_data(request):
    items = TypeOfCar.objects.all()
    context = {
        'items' : items,
    }
    return render(request, 'dashboard/car.html',context)

@login_required
def crashtype_data(request):
    items = TypeOfCrash.objects.all()
    context = {
        'items' : items,
    }
    return render(request, 'dashboard/crashtype.html',context)

@login_required
def damage_data(request):
    items = Damage.objects.all()
    context = {
        'items' : items,
    }
    return render(request, 'dashboard/damage.html',context)

@login_required
def sight_data(request):
    items = DriverSight.objects.all()
    context = {
        'items' : items,
    }
    return render(request, 'dashboard/sight.html',context)

