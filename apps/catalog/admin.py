from django.contrib import admin


from .models import (
    Product,
    ProductVariant,
    Attribute,
    AttributeValue,
    Brand,
    Category,
)
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

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "parent",
        "is_active",
        "sort_order",
    )

    list_filter = (
        "is_active",
    )

    search_fields = (
        "name",
        "slug",
    )

    list_editable = (
        "sort_order",
        "is_active",
    )

    ordering = (
        "sort_order",
        "name",
    )
    
