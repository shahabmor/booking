from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models

class User(AbstractUser):

    phone_number = models.PositiveBigIntegerField(unique=True, validators=[
            RegexValidator(r'^989[0-3,9]\d{8}$', 'Enter a valid phone number.', 'invalid')
    ])
    birthday = models.DateField(null=True, blank=True)
    avatar = models.ImageField(null=True, blank=True)

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email", "phone_number"]