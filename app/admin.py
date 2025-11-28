from django.contrib import admin

from .models import Task, Comment, Review, Product, CartItem, Order

admin.site.register(Task)
admin.site.register(Comment)
admin.site.register(Review)
admin.site.register(Product)
admin.site.register(CartItem)
admin.site.register(Order)