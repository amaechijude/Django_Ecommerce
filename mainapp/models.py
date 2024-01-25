from django.db import models

from django.utils.html import mark_safe
from django.conf import settings

# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

class Customers(models.Model):
    CustomerID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=100)
    Email = models.EmailField()
    PasswordHash = models.CharField(max_length=100)#to be modified later
    IsAdmin = models.CharField(max_length=100)#to be modified later
    
    def __str__(self):
        return (f"{self.Name}")

class Orders(models.Model):
    OrderID = models.AutoField(primary_key=True)
    CustomerID = models.ForeignKey(Customers, on_delete=models.CASCADE)
    CreatedAt = models.DateTimeField(auto_now_add=True)

class OrderItems(models.Model):
    OrderItemID = models.AutoField(primary_key=True)
    OrderID = models.ForeignKey(Orders, on_delete=models.CASCADE)
    BookID = models.ForeignKey(Books, on_delete=models.CASCADE)
    Quantity = models.IntegerField()
    Price = models.FloatField()

class Payments(models.Model):
    PaymentID = models.AutoField(primary_key=True)
    OrderID = models.ForeignKey(Orders, on_delete=models.CASCADE)
    Amount = models.FloatField()
    PaymentDate = models.DateTimeField(auto_now_add=True)


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