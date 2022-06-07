from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.

class User(AbstractUser):
    is_cust = models.BooleanField(default=False)
    is_vendor = models.BooleanField(default=False)

class CustProfileInfo(models.Model):
    cust_user = models.ForeignKey(User,on_delete=models.CASCADE)

    #additional
    Name = models.CharField(max_length=240,unique=False)
    Phone = models.IntegerField(validators=[MinValueValidator(1000000000),
                                       MaxValueValidator(9999999999)],unique=True)
    Address=models.CharField(max_length=240,unique=False)
    Zipcode=models.IntegerField(validators=[MinValueValidator(100000),
                                       MaxValueValidator(999999)],unique=False)

    def __str__(self):
        return self.user.username

class VendorProfileInfo(models.Model):
    vendor_user = models.ForeignKey(User,on_delete=models.CASCADE)

    #additional
    Name = models.CharField(max_length=240,unique=False)
    Phone = models.IntegerField(validators=[MinValueValidator(1000000000),
                                       MaxValueValidator(9999999999)],unique=True)
    Shop_Name = models.CharField(max_length=240,unique=False)

    def __str__(self):
        return self.user.username
