from django.db import models
from django.contrib.auth import get_user_model
from django.core import validators

User = get_user_model()


class Profile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True

    )
    first_name = models.CharField(max_length=255, blank=True, default='')
    last_name = models.CharField(max_length=255, blank=True, default='')
    email = models.EmailField(blank=True, default='please_change@hotmail.com')
    date_of_birth = models.DateField(blank=True, default='1990-01-01')
    bio = models.CharField(max_length=255, default='please change', blank=True,
                           validators=[validators.MinLengthValidator(10)])
    avatar = models.ImageField(blank=True, null=True,
                               upload_to='test/')
