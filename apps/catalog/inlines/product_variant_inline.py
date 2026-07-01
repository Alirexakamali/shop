from django.contrib import admin

from ..models import ProductVariant


class ProductVariantInline(admin.TabularInline):
    model = ProductVariant
    extra = 0

    fields = (
        "sku",
        "price",
        "discount_price",
        "is_active",
    )

    show_change_link = True
