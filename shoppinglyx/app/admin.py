from django.contrib import admin

from .models import Cart, Customer, Product, OrderPlaced


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "name", "city", "locality", "zipcode", "division")


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "category",
        "brand",
        "selling_price",
        "discount_price",
        "product_image",
    )


@admin.register(OrderPlaced)
class OrderPlacedAdmin(admin.ModelAdmin):
    list_display = ("id", "quantity", "ordered_date", "status")


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ("id", "quantity")
