from venv import create
from django.db import models
from crossmlassignment.choice import *
from django.contrib.auth.models import User

# Create your models here.

class Card(models.Model):
    created_date = models.DateField(auto_now_add=True)
    type = models.SmallIntegerField(choices=Type.CHOICES,null=False,blank=False)
    priority = models.SmallIntegerField(choices=Priority.CHOICES,null=False,blank=False)
    status = models.SmallIntegerField(choices=Status.CHOICES,null=False,blank=False)
    assignee = models.ForeignKey(User,on_delete=models.DO_NOTHING)