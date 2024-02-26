from django.contrib import admin
from .models import Client, Product, Order


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone_number', 'address', 'registration_date')
    search_fields = ('name', 'email')
    list_filter = ('registration_date',)  # Фильтр по дате регистрации


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity', 'added_date')
    search_fields = ('name',)
    list_filter = ('added_date',)  # Фильтр по дате добавления


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'client', 'total_amount', 'order_date')
    search_fields = ('client__name', 'total_amount')
    list_filter = ('order_date', 'client')  # Фильтр по дате заказа и по клиенту
