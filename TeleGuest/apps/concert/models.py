from TeleGuest.apps.teleguestAuth.models import User
from django.db import models

class Concert(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=40)
    singer = models.CharField(max_length=20)
    price = models.IntegerField(default=0)
    concert_date = models.DateField()
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=13)
    reservations = models.ManyToManyField(User, related_query_name='reservates_concerts')
    