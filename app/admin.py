from django.contrib import admin

from .models import Task, Comment, Review, Product, CartItem, Order

admin.site.register(Task)
admin.site.register(Comment)
admin.site.register(Review)
admin.site.register(Product)
admin.site.register(CartItem)

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
        ('Товары', {
            'fields': ('items',)
        }),
    )
    
    def get_readonly_fields(self, request, obj=None):
        if obj:  # Editing an existing object
            return self.readonly_fields + ('user', 'is_paid')
        return self.readonly_fields