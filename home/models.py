# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Hyrety(models.Model):

    #__Hyrety_FIELDS__
    tile = models.TextField(max_length=255, null=True, blank=True)
    younrre = models.CharField(max_length=255, null=True, blank=True)
    utuy = models.BooleanField()
    ttt = models.DateTimeField(blank=True, null=True, default=timezone.now)

    #__Hyrety_FIELDS__END

    class Meta:
        verbose_name        = _("Hyrety")
        verbose_name_plural = _("Hyrety")


class Employee(models.Model):

    #__Employee_FIELDS__
    name = models.TextField(max_length=255, null=True, blank=True)
    hello = models.BooleanField()

    #__Employee_FIELDS__END

    class Meta:
        verbose_name        = _("Employee")
        verbose_name_plural = _("Employee")



#__MODELS__END
