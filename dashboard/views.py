from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import CarCrashRandom
from .forms import CrashForm
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
def order(request):
    return render(request, 'dashboard/orders.html')

