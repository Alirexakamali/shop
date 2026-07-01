from django.contrib import admin

from ..models import ProductVariantAttribute


class ProductVariantAttributeInline(admin.TabularInline):
    model = ProductVariantAttribute
    extra = 0

    autocomplete_fields = (
        "attribute",
        "value",
    )
