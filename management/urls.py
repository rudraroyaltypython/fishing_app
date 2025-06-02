from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),  # Main login page
    path('login/', views.custom_login, name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('worker-dashboard/', views.worker_dashboard, name='worker_dashboard'),
    path('fish-inventory/', views.fish_inventory_list, name='fish_inventory_list'),
    path('fish-inventory/add/', views.fish_inventory_add, name='fish_inventory_add'),
]
