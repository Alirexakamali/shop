from ..models import ProductVariantAttribute
from django.contrib import admin

class ProductVariantAttributeInline(admin.TabularInline):
    model = ProductVariantAttribute
    extra = 1