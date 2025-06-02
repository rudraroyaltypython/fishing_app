from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .models import Profile
from .models import FishInventory
from django.contrib.auth.models import User
from django.contrib import messages

def home(request):
    return render(request, 'management/home.html')

def custom_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            if user.is_superuser:
                return redirect('admin_dashboard')
            else:
                return redirect('worker_dashboard')
        else:
            messages.error(request, 'Invalid username or password.')

    return render(request, 'management/login.html')  # This ensures CSRF token works
@login_required
def admin_dashboard(request):
    return render(request, 'management/admin_dashboard.html')

@login_required
def worker_dashboard(request):
    return render(request, 'management/worker_dashboard.html')


@login_required
def fish_inventory_list(request):
    fish_list = FishInventory.objects.all().order_by('-date_added')
    return render(request, 'management/fish_inventory_list.html', {'fish_list': fish_list})

@login_required
def fish_inventory_add(request):
    if not request.user.profile.role == 'admin':
        return redirect('fish_inventory_list')

    if request.method == 'POST':
        fish_type = request.POST.get('fish_type')
        quantity_kg = request.POST.get('quantity_kg')
        quality_grade = request.POST.get('quality_grade')
        storage_location = request.POST.get('storage_location')

        FishInventory.objects.create(
            fish_type=fish_type,
            quantity_kg=quantity_kg,
            quality_grade=quality_grade,
            storage_location=storage_location,
            added_by=request.user
        )
        return redirect('fish_inventory_list')

    return render(request, 'management/fish_inventory_add.html')
