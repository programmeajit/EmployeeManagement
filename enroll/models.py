from django.db import models

class Employee(models.Model):
    empId = models.CharField(max_length=100)
    empName = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    department = models.CharField(max_length=70)
    joindate = models.DateField()

# Create your models here.
