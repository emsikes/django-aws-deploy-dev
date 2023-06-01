from django.db import models
from django.contrib.auth.models import User
from django.conf import settings



class Profile(models.Model):
    profile_pic = models.ImageField(null=True, blank=True, default='default.jpg')
    # FK
    user = models.ForeignKey(User, max_length=10, on_delete=models.CASCADE, null=True)
    