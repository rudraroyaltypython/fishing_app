from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('worker', 'Factory Worker'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)

    def __str__(self):
        return f"{self.user.username} - {self.role}"


class FishInventory(models.Model):
    FISH_TYPES = [
        ('salmon', 'Salmon'),
        ('tuna', 'Tuna'),
        ('mackerel', 'Mackerel'),
        ('prawns', 'Prawns'),
        ('other', 'Other'),
    ]

    fish_type = models.CharField(max_length=50, choices=FISH_TYPES)
    quantity_kg = models.FloatField()
    quality_grade = models.CharField(max_length=20)  # e.g., A, B, C
    date_added = models.DateField(auto_now_add=True)
    added_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    storage_location = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.fish_type} - {self.quantity_kg} kg"