from django.db import models

from django.utils.html import mark_safe
from django.conf import settings

# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

class Item(models.Model):
    ItemID = models.AutoField(primary_key=True)
    Title = models.CharField(max_length=100)
    Price = models.FloatField()
    Stock = models.IntegerField()
    
    def __str__(self):
        return (f"{self.Title}")


class Customer(models.Model):
    CustomerID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=100)
    Email = models.EmailField()
    Address = models.CharField(max_length=100)
    Phone_No = models.CharField(max_length=14)
    image = models.ImageField(upload_to='customers')
    
    def __str__(self):
        return (f"{self.Name}")

class Order(models.Model):
    OrderID = models.AutoField(primary_key=True)
    CustomerID = models.ForeignKey(Customer, on_delete=models.CASCADE)
    CreatedAt = models.DateTimeField(auto_now_add=True)

class OrderItem(models.Model):
    OrderItemID = models.AutoField(primary_key=True)
    OrderID = models.ForeignKey(Order, on_delete=models.CASCADE)
    ItemID = models.ForeignKey(Item, on_delete=models.CASCADE)
    Quantity = models.IntegerField()
    Price = models.FloatField()

class Payment(models.Model):
    PaymentID = models.AutoField(primary_key=True)
    OrderID = models.ForeignKey(Order, on_delete=models.CASCADE)
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