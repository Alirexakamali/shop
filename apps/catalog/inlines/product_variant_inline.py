from ..models import ProductVariant
from django.contrib import admin


class ProductVariantInline(admin.TabularInline):
    model = ProductVariant
    extra = 1
