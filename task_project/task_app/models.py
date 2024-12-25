from django.db import models
from django.db import models
from django.contrib.auth.models import AbstractUser, User
from django.utils import timezone
# Create your models here.
# users/models.py


class User(User):
    mobile_number = models.CharField(max_length=15)
    address = models.CharField(max_length=255)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)

class Task(models.Model):
    STATUS_CHOICES = [
        ('assigned', 'Assigned'),
        ('pending', 'Pending'),
        ('not_assigned', 'Not Assigned'),
        ('completed', 'Completed'),
    ]
    name = models.CharField(max_length=100)
    assigned_to = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks')
    due_date = models.DateTimeField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='not_assigned')
    created_at = models.DateTimeField(auto_now_add=True)
