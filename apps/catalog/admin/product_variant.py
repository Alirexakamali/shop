from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from ..models import ProductVariant
from ..inlines import ProductImageInline, ProductVariantAttributeInline


@admin.register(ProductVariant)
class ProductVariantAdmin(admin.ModelAdmin):
    inlines = [
        ProductImageInline,
        ProductVariantAttributeInline,
    ]

    list_display = (
        "id",
        "product",
        "sku",
        "price",
        "discount_price",
        "is_active",
    )

    list_filter = (
        "is_active",
        "product__category",
        "product__brand",
    )

    search_fields = (
        "sku",
        "barcode",
        "product__name",
    )

    autocomplete_fields = ("product",)

    readonly_fields = (
        "created_at",
        "updated_at",
    )

    list_editable = ("is_active",)

    list_select_related = ("product",)

    ordering = ("-created_at",)

    list_per_page = 25

    fieldsets = (
        (
            _("Product"),
            {"fields": ("product",)},
        ),
        (
            _("Pricing"),
            {
                "fields": (
                    "price",
                    "discount_price",
                )
            },
        ),
        (
            _("Identifiers"),
            {
                "fields": (
                    "sku",
                    "barcode",
                )
            },
        ),
        (
            _("Shipping"),
            {"fields": ("weight",)},
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
