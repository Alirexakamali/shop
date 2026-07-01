from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from ..models import Product

from ..inlines import ProductVariantInline


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [
        ProductVariantInline,
    ]

    list_display = (
        "id",
        "name",
        "category",
        "brand",
        "is_active",
        "created_at",
    )

    list_filter = (
        "category",
        "brand",
        "is_active",
    )

    search_fields = (
        "name",
        "slug",
    )

    autocomplete_fields = (
        "category",
        "brand",
    )

    readonly_fields = (
        "created_at",
        "updated_at",
    )

    list_editable = ("is_active",)

    list_per_page = 25

    ordering = ("-created_at",)

    list_select_related = (
        "category",
        "brand",
    )

    fieldsets = (
        (
            _("Basic Information"),
            {
                "fields": (
                    "name",
                    "slug",
                    "category",
                    "brand",
                )
            },
        ),
        (
            _("Description"),
            {
                "fields": (
                    "short_description",
                    "description",
                )
            },
        ),
        (
            _("Status"),
            {"fields": ("is_active",)},
        ),
        (
            _("Metadata"),
            {
                "fields": (
                    "created_at",
                    "updated_at",
                )
            },
        ),
    )
