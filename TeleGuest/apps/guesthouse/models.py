from django.db import models
from TeleGuest.apps.teleguestAuth.models import User

class Guesthouse(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=40)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=13)
    concert_date = models.DateField()
    reservations = models.ManyToManyField(User)
    pub_date = models.DateField(auto_now=True)