from django.db import models

# Create your models here.


class Employee(models.Model):
    fullname = models.CharField(max_length=100)
    emp_code = models.CharField(max_length=30)
    mobile = models.CharField(max_length=15)
    email_id = models.CharField(max_length=30)


# by default class name in table name if not defined