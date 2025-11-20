from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    username = models.CharField(max_length=60)
    first_name = models.CharField(max_length=60, blank=True)
    last_name = models.CharField(max_length=60, blank=True)
    file = models.FileField(blank=True)
    location = models.CharField(blank=True)
    tel = models.IntegerField(blank=True, null=True)
    description = models.CharField(max_length=500,blank=True)
    working_hours = models.CharField(blank=True)
    type = models.CharField(choices=[('customer', 'customer'), ('business', 'business')])
