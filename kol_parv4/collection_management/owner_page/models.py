from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
# pip install django-phonenumber-field phonenumbers
from phonenumber_field.modelfields import PhoneNumberField


class Users(AbstractUser):
    
    username = models.CharField(
        max_length=150,
        unique=True,
        primary_key=True,
        help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.',
        validators=[RegexValidator(r'^[\w.@+-]+$')],
        error_messages={
            'unique': "A user with that username already exists.",
        },
    )
    
    Show = models.BooleanField(default=False)

    Telephone = PhoneNumberField(blank=True)

    def __str__(self):
        return str(self.username)
