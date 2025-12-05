from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Review(models.Model):

    reviewer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='customer_review')
    business_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='review')
    rating = models.PositiveSmallIntegerField(choices=[(1, "1"), (2, "2"), (3, "3"), (4, "4"), (5, "5")])
    description = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    uploaded_at = models.DateTimeField(auto_now=True)