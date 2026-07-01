from django.contrib import admin

from .models import Shipment, ShippingMethod


@admin.register(ShippingMethod)
class ShippingMethodAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "price",
        "estimated_days",
        "is_active",
    )

    list_editable = (
        "price",
        "is_active",
    )


@admin.register(Shipment)
class ShipmentAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "order",
        "shipping_method",
        "tracking_code",
        "status",
    )

    list_filter = (
        "status",
        "shipping_method",
    )

    autocomplete_fields = (
        "order",
        "shipping_method",
    )

    search_fields = (
        "tracking_code",
    )