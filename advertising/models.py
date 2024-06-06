from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Advertiser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.name


class Location(models.Model):
    name = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return self.name


class Ad(models.Model):
    advertiser = models.ForeignKey(Advertiser, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    spend = models.DecimalField(max_digits=10, decimal_places=2)
    crypto_acquired = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.title


class Transaction(models.Model):
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    crypto_amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.ad.title} - {self.amount} - {self.crypto_amount}"
