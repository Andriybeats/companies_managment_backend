from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=25, blank=False)
    surname = models.CharField(max_length=25, blank=False)
    address = models.CharField(max_length=25, blank=True)
    city_birthday = models.CharField(max_length=25, blank=True)
    date_birthday = models.DateField()
    start_work = models.DateField()
