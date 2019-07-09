from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.contrib.auth.models import User


# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    image = models.ImageField(default = 'default.jpg',upload_to = 'profile_pics')

    def __str__(self):
        return f'{self.user.username} profile'

# 
# @receiver(post_save,sender = User)
# def create_profile(sender,instance,created, **kwargs):
#     if created:
#         profile.objects.create(user = instance)
#
#
# @reciever(post_save,sender = User)
# def save_Profile(sender,instance,**kwargs):
#     instance.profile.save()
