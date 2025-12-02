from django.contrib import admin
from .models import Supplier, Product, Order, OrderItem

admin.site.register(Supplier)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderItem)
