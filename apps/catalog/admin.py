from django.contrib import admin
from .models import Product, ProductVariant
from .inlines import (
    ProductVariantInline,
    ProductImageInline,
    ProductVariantAttributeInline,
)

# Register your models here.


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "category",
        "brand",
        "is_active",
    )

    search_fields = (
        "name",
        "slug",
    )

    list_filter = (
        "category",
        "brand",
        "is_active",
    )

    inlines = [
        ProductVariantInline,
    ]


@admin.register(ProductVariant)
class ProductVariantAdmin(admin.ModelAdmin):
    list_display = (
        "product",
        "sku",
        "price",
        "is_active",
    )

    inlines = [
        ProductImageInline,
        ProductVariantAttributeInline,
    ]
