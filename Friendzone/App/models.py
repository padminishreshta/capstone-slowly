from django.db import models
from django.contrib.postgres.fields import ArrayField
# Create your models here.

class Account(models.Model):
    User = models.CharField(max_length=200)
    Age = models.IntegerField()
    Email = models.CharField(max_length=200)
    Password = models.CharField(max_length=200)
    def __str__(self):
        return self.User    

class Account_Holder(models.Model):
    User = models.ForeignKey(Account,max_length=200,on_delete=models.CASCADE)
    Interests = ArrayField(
            models.CharField(max_length=200, blank=True),
            size=8,
        )
    Friends = ArrayField(
            models.CharField(max_length=200, default="True"),
            size=100,
        ) 
    def __str__(self):
        return self.User    
