from django.db import models
from django.contrib.postgres.fields import ArrayField
# Create your models here.

class Account(models.Model):
    User = models.CharField(max_length=200)
    Age = models.IntegerField()
    Email = models.CharField(max_length=200)
    Password = models.CharField(max_length=200)
    Interests = ArrayField(
            models.CharField(max_length=200, blank=True),
            size=8,
        )
    def __str__(self):
        return self.User    

class Friends_setup(models.Model):
    User = models.ForeignKey(Account,null=True,on_delete=models.SET_NULL)
    Friends = models.ManyToManyField('self', null=True, blank=True)
    def __str__(self):
        return self.User+"'s"+" Friendslist"    