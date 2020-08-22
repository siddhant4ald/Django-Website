from django.db import models
from django.contrib.auth.models import User



class Student(models.Model):
    sid=models.IntegerField(primary_key=True)
    sname=models.CharField(max_length=50)
    semail=models.CharField(max_length=50)
    scity=models.CharField(max_length=120)
    sage=models.IntegerField(null=True)


class todo(models.Model):
	content=models.TextField()



# Create your models here.

class Task(models.Model):
	title = models.CharField(max_length=200)
	complete = models.BooleanField(default=False)
	created = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.title