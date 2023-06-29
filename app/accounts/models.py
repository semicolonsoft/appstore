from django.db import models
from django.db.models import Sum
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    phone = models.CharField(max_length=15, null=True, blank=True, unique=True)
    is_developer = models.BooleanField(default=False)
    image = models.ImageField(upload_to='profiles', null=True, blank=True)


    REQUIRED_FIELDS = []
    USERNAME_FIELD = 'phone'
