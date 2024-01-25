from django.db import models

from django.utils.html import mark_safe
from django.conf import settings

# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    address = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.user.username}"
    

class Category(models.Model):
    Category_ID = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='category')

    class Meta:
        verbose_name_plural = "Categories"
    
    def __str__(self):
        return f'{self.title}'


class Vendor(models.Model):
    VendorID = models.AutoField(primary_key=True)
    Store_Name = models.CharField(max_length=100)
    Vendor_Image = models.ImageField(upload_to="vendor")
    Address = models.CharField(max_length=100)
    Description = models.TextField(null=True, blank=True)


    def __str__(self):
        return f'{self.title}'