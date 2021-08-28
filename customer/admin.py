from django.contrib import admin
from .models import OrderModel,Category,MenuItem
# Register your models here.

admin.site.register(OrderModel)
admin.site.register(MenuItem)
admin.site.register(Category)