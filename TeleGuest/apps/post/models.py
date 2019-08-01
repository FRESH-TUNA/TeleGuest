from django.db import models
from TeleGuest.apps.teleguestAuth.models import User

class Post(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    participants = models.ManyToManyField(User, related_query_name='participate_posts')
    post_title = models.CharField(max_length=60)
    concert_date = models.DateField()
    description = models.CharField(max_length=1000, blank=True)
    now_capacity = models.IntegerField(default=0)
    max_capacity = models.IntegerField(default=0)
    pub_date = models.DateField(auto_now=True)
