from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Product(models.Model):
    pid=models.IntegerField(primary_key=True)
    pname=models.CharField(max_length=20)
    pcost=models.DecimalField(max_digits=10,decimal_places=2)
    pmfdt=models.DateField()
    pexpdt=models.DateField()
class Review(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE,related_name='reviews')
    title=models.CharField(max_length=250)
    review=models.TextField()
    rating=models.IntegerField()
    created_by=models.ForeignKey(User,on_delete=models.CASCADE,null=True,)
