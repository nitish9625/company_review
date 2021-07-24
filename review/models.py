from django.contrib.auth.models import User
from django.db import models

# Create your models here.

#company model
class Company(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=1000)
    category = models.CharField(max_length=100)
    net_worth = models.CharField(max_length=200)

    def __str__(self):
        return self.name
# company review model
class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    comment = models.TextField(max_length=300)
    rate = models.IntegerField(default=0)
    createTime = models.DateTimeField(auto_now_add=True)
