from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
import datetime

# Create your models here.

class StudentRecords(AbstractUser):
    date = datetime.datetime.now()
    year = int(date.year)

    username = models.CharField(max_length=150, unique = False)
    rollNo = models.PositiveIntegerField(unique = True)
    dateIssued = models.DateField(default=date.strftime('%Y-%m-%d'))
    yearOfAdmission = models.PositiveIntegerField(default=year)
    name = models.CharField(max_length = 50)
    branch = models.CharField(max_length = 50)
    emailId = models.EmailField(max_length=100, null=True)
    phoneNo = models.PositiveIntegerField(null=True)

    book1 = models.CharField(null=True, max_length=50, default="None")
    book1_date = models.DateField(default=date.strftime('%Y-%m-%d'))
    book2 = models.CharField(null=True, max_length=50, default="None")
    book2_date = models.DateField(default=date.strftime('%Y-%m-%d'))
    book3 = models.CharField(null=True, max_length=50, default="None")
    book3_date = models.DateField(default=date.strftime('%Y-%m-%d'))

    REQUIRED_FIELDS = ['name']
    USERNAME_FIELD = 'rollNo'

    def get_absolute_url(self):
        return reverse('mainpage')

    def __str__(self):
        return self.rollNo