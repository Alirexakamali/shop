from ..models import ProductImage
from django.contrib import admin

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1