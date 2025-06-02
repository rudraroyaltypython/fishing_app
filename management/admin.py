from django.contrib import admin
from .models import Profile
from .models import FishInventory


@admin.register(FishInventory)
class FishInventoryAdmin(admin.ModelAdmin):
    list_display = ('fish_type', 'quantity_kg', 'quality_grade', 'date_added', 'added_by', 'storage_location')
    search_fields = ['fish_type', 'storage_location', 'added_by__username']
    list_filter = ['fish_type', 'quality_grade', 'date_added']


    
admin.site.register(Profile)


