from django.db import models




# Create your models here.
class Companyreg(models.Model):
    userid =models.CharField(max_length=10)
    password =models.CharField(max_length=20)

class Add_company(models.Model):
    name = models.CharField(max_length=20)
    symbol=models.CharField(max_length=20)
    password=models.CharField(max_length=20)
    email=models.EmailField(max_length=20)
    address=models.CharField(max_length=20)
    phonenumber=models.IntegerField()
    select =models.CharField(max_length=20)
    image=models.ImageField(upload_to="product_image/")