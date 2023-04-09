from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import TextChoices, CharField


# Create your models here.

class User(AbstractUser):
    class personality(TextChoices):
        MERCHANT = 'merchant', 'sotuvchi'
        CLIENT = 'client', 'xaridor'

    person = CharField(max_length=35, choices=personality.choices, default=personality.MERCHANT)

