from django.contrib import admin
from ..models import Category

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