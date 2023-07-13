
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    user_name = models.CharField(max_length=10, null=True)
    age = models.IntegerField(null=True)
    gender = models.CharField(max_length=10, null=True)

class Meta(AbstractUser.Meta):
    swappable = 'AUTH_USER_MODEL'
    related_name = 'travelingbears_user_groups'
    related_query_name = 'travelingbears_user'

    
    def __str__(self):
        return self.username
