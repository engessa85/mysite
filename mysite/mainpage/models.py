from django.db import models

# Create your models here.

class user_service(models.Model):
    name = models.CharField(max_length = 75)
    email = models.EmailField(max_length = 75)
    phone = models.EmailField(max_length = 75)
    whats = models.EmailField(max_length = 75)
    services = models.EmailField(max_length = 75)
    text = models.TextField()


class user_issue(models.Model):
    name = models.CharField(max_length = 75)
    email = models.EmailField(max_length = 75)
    text = models.TextField()
