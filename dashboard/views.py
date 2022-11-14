from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import CarCrashRandom
from .forms import CrashForm

# Create your views here.
#Admin Views
@login_required
def index(request):
    return render(request, 'dashboard/index.html')

@login_required
def staff(request):
    return render(request, 'dashboard/staff.html')

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
def order(request):
    return render(request, 'dashboard/orders.html')
