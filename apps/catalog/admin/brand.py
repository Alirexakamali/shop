from django.contrib import admin

from ..models import Brand

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "is_active",
    )

    search_fields = (
        "name",
        "slug",
    )

    list_filter = (
        "is_active",
    )

    list_editable = (
        "is_active",
    )