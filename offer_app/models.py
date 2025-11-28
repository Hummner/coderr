from django.db import models
from django.contrib.auth.models import User

# Create your models here.


def user_directory_path(instance, filename):
    
    ext = filename.split('.')[-1]
    filename = f"offerImg.{ext}"
    return "user_{0}/{1}".format(instance.user.id, filename)


class Offer(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="offer")
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=250)
    image = models.FileField(upload_to=user_directory_path, blank=True, null=True)


class OfferDetails(models.Model):
    offer = models.ForeignKey(Offer, on_delete=models.CASCADE, related_name='offer_detail')
    title = models.CharField(max_length=200)
    revisions = models.IntegerField()
    delivery_time_in_days = models.IntegerField()
    price = models.IntegerField()
    features = models.JSONField(default=list)
    offer_type = models.CharField(choices=[('basic', 'basic'), ('standard', 'standard'), ('premium', 'premium')])

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['offer', 'offer_type'], name='unique_offer_type_per_offer'
            )
        ]
