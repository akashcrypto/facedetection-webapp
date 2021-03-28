from django.db import models

# Create your models here.
class User(models.Model):
    email = models.CharField(max_length=20, primary_key=True)
    fullname = models.CharField(max_length=50)
    code = models.IntegerField()
    phone_number = models.IntegerField(default=0)
    job = models.CharField(max_length=20)
    pwd = models.CharField(max_length=20)
