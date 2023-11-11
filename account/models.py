from ast import Compare
from operator import mod
from tabnanny import verbose
from django.db import models
from django.db.models.base import Model
from django.contrib.auth.models import AbstractUser
from django.db.models.fields import BigIntegerField, BooleanField
from django.db.models.fields.related import ForeignKey
from django.utils import timezone
from django.utils.html import mark_safe

from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.


class User(AbstractUser):
    pass


    class Meta:
        verbose_name = "یوزر"
        verbose_name_plural = "یوزر ها"

