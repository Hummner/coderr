from django.db import models
from django.contrib.auth.models import User
from .storage import overwirte_storage

# Create your models here.

def user_directory_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = f"profileImg.{ext}"
    return "user_{0}/{1}".format(instance.user.id, filename)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile", primary_key=True)
    username = models.CharField(max_length=60)
    first_name = models.CharField(max_length=60, blank=True)
    last_name = models.CharField(max_length=60, blank=True)
    file = models.FileField(upload_to=user_directory_path, blank=True, storage=overwirte_storage)
    location = models.CharField(max_length=200, blank=True)
    tel = models.CharField(blank=True, max_length=30)
    description = models.CharField(max_length=500,blank=True)
    working_hours = models.CharField(blank=True, max_length=30)
    email = models.EmailField(blank=True)
    created_at = models.DateTimeField(auto_now=True)
    type = models.CharField(choices=[('customer', 'customer'), ('business', 'business')])


# class BusinessProfiles(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile", primary_key=True)
#     username = models.CharField(max_length=60)
#     first_name = models.CharField(max_length=60, blank=True)
#     last_name = models.CharField(max_length=60, blank=True)
#     file = models.FileField(upload_to=user_directory_path, blank=True, storage=overwirte_storage)
#     location = models.CharField(max_length=200, blank=True)
#     tel = models.CharField(blank=True, max_length=30)
#     description = models.CharField(max_length=500,blank=True)
#     working_hours = models.CharField(blank=True, max_length=30)
#     type = models.CharField(choices=[('customer', 'customer'), ('business', 'business')])

# class CustomerProfiles(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile", primary_key=True)
#     username = models.CharField(max_length=60)
#     first_name = models.CharField(max_length=60, blank=True)
#     last_name = models.CharField(max_length=60, blank=True)
#     file = models.FileField(upload_to=user_directory_path, blank=True, storage=overwirte_storage)
#     location = models.CharField(max_length=200, blank=True)
#     tel = models.CharField(blank=True, max_length=30)
#     description = models.CharField(max_length=500,blank=True)
#     working_hours = models.CharField(blank=True, max_length=30)
#     type = models.CharField(choices=[('customer', 'customer'), ('business', 'business')])
