from django.test import TestCase
from .models import *
'''
# Create your tests here.
class UnparticipateTests(TestCase):
    def unparticipate(self, email, password):
        member = Member.objects.filter(email=email)
        if member[0].pwd == request.POST['pwd']:
            post = get_object_or_404(Post,id=pk)
            post.now_capacity = post.now_capacity -1
            post.save()
            member[0].delete()
'''       