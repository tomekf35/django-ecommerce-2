from django.contrib import admin
from .models import Category, Product, Review


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "slug"]
    prepopulated_fields = {"slug": ("name",)}
    search_fields = ["name"]


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "seller",
        "category",
        "price",
        "available",
        "created_at",
        "updated_at",
    ]
    prepopulated_fields = {"slug": ("name", "seller")}
    list_filter = [
        "name",
        "seller",
        "category",
        "price",
        "available",
    ]
    search_fields = ["name", "seller"]
    raw_id_fields = [
        "seller",
    ]


admin.site.register(Review)
