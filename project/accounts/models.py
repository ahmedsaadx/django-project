from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField

class CustomUser(AbstractUser):
    email = models.EmailField(('email address'), unique=True)
    phone = PhoneNumberField(null=False, blank=False, unique=True)
