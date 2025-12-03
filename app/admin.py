from django.contrib import admin

from .models import Task, Comment, Review, Product, CartItem, Order, Manager, OrderItem

admin.site.register(Task)
admin.site.register(Comment)
admin.site.register(Review)
admin.site.register(Product)
admin.site.register(CartItem)

@admin.register(Manager)
class ManagerAdmin(admin.ModelAdmin):
    list_display = ('user', 'date_created')
    search_fields = ('user__username',)
    readonly_fields = ('date_created',)

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'quantity', 'product_price', 'order')
    search_fields = ('product_name', 'order__id')
    readonly_fields = ('order', 'product_name', 'product_price', 'manufacturer', 'description', 'image')

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'total_price', 'status', 'is_paid', 'date_created')
    list_filter = ('status', 'is_paid', 'date_created')
    search_fields = ('user__username', 'id')
    readonly_fields = ('date_created', 'total_price')
    fieldsets = (
        ('Информация о заказе', {
            'fields': ('user', 'total_price', 'date_created', 'is_paid')
        }),
        ('Статус', {
            'fields': ('status',)
        }),
    )
    
    def get_readonly_fields(self, request, obj=None):
        if obj:  # Editing an existing object
            return self.readonly_fields + ('user', 'is_paid')
        return self.readonly_fields