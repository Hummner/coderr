from django.db import models
from django.contrib.auth.models import User
from offer_app.models import OfferDetails

# Create your models here.


class Order(models.Model):
    customer_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='custmer_orders')
    business_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='business_orders')
    title = models.CharField(max_length=200)
    revisions = models.IntegerField()
    delivery_time_in_days = models.IntegerField()
    price = models.IntegerField()
    features = models.JSONField(default=list)
    offer_type = models.CharField(choices=[('basic', 'basic'), ('standard', 'standard'), ('premium', 'premium')])
    status = models.CharField(choices=[('in_progress', 'in_progress'), ('completed', 'completed')], default="in_progress")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    offer_detail = models.ForeignKey(OfferDetails, on_delete=models.CASCADE, related_name='order_offer_detail')


class OrderCountInProgress(models.Model):
    pass