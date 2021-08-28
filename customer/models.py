from django.db import models
from django.db.models.base import Model

# Create your models here.

class MenuItem(models.Model):
    name=models.CharField(max_length=120)
    description=models.TextField()
    image=models.ImageField(upload_to='menu_images')
    price=models.DecimalField(max_digits=5, decimal_places=2)
    category=models.ManyToManyField('Category', related_name='item')

    def __str__(self):
        return str('Product Name : '+self.name)

class Category(models.Model):
    name=models.CharField(max_length=120)

    def __str__(self):
        return str(self.name)

class OrderModel(models.Model):
    created=models.DateTimeField(auto_now_add=True)
    price= models.DecimalField(max_digits=7, decimal_places=2)
    items=models.ManyToManyField('MenuItem', related_name='order', blank=True)
    name=models.CharField(max_length=100, blank=True)
    email=models.CharField(max_length=120, blank=True)
    street=models.CharField(max_length=120, blank=True)
    city=models.CharField(max_length=120, blank=True)
    state=models.CharField(max_length=120, blank=True)
    zip_code=models.IntegerField(blank=True, null=True)
    is_paid=models.BooleanField(default=False)
    is_shipped=models.BooleanField(default=False)
    def __str__(self):
        return f'Order:{self.created.strftime("%b %d %I: %M %p")}'


