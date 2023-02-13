from django.db import models
from datetime import date
from django.contrib.auth.models import User


class ProfileResults(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=1)
    two_by_two = models.CharField(max_length=30)
    three_by_three = models.CharField(max_length=30)
    four_by_four = models.CharField(max_length=30)


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=1)
    signup_date = models.DateField(default=date.today)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
