from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class user_service(models.Model):
    services_choice = (('Home Work','Home Work') , ('Project','Project') , ('Course','Course'))
    title = models.CharField(max_length = 75)
    services = models.CharField(max_length = 75 , choices = services_choice)
    subject = models.TextField()
    email = models.CharField(max_length=75,blank=False, null= True)
    whatsapp_number = models.IntegerField(blank=False, null= True)
    country = models.CharField(max_length = 75 ,blank=False, null= True)
    delivery_date =models.DateField(blank = True , null = True)
    file = models.FileField(blank = True)
    author = models.ForeignKey(User,default = None,on_delete=models.CASCADE)

    solving = models.BooleanField(default=False)
    rejected = models.BooleanField(default=False)
    accepted = models.BooleanField(default=False)
    in_progress = models.BooleanField(default=False)
    finished = models.BooleanField(default=False)






class user_issue(models.Model):
    name = models.CharField(max_length = 75)
    email = models.EmailField(max_length = 75)
    text = models.TextField()
