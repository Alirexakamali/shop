from ..models import ProductImage
from django.contrib import admin

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 0

    fields = (
        "image",
        "alt",
        "is_main",
        "sort_order",
    )