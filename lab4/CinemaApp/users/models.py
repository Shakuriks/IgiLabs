from django.db import models
from django.contrib.auth.models import AbstractUser 
from django.core.validators import RegexValidator


class User(AbstractUser):
     phone_number = models.CharField(validators=[RegexValidator(regex=r'^\+375 \(29\) \d{7}$', message = "Формат номера телефона: +375 (29) XXXXXXX")], max_length=17, blank=True)
