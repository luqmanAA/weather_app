from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.db import models

# Create your models here.


class User(AbstractUser):
    username = None
    email = models.EmailField(
        _("email address"),
        max_length=200,
        unique=True,
        error_messages={
            'unique': 'A user with this email already exists!'
        }
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
