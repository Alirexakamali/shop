from django.contrib import admin

from .models import Order, OrderItem


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderItemInline]

    list_display = (
        "id",
        "user",
        "status",
        "total_amount",
        "created_at",
    )

    list_filter = (
        "status",
    )

    autocomplete_fields = (
        "user",
        "address",
    )

    search_fields = (
        "user__phone",
        "user__email",
    )


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = (
        "order",
        "variant",
        "quantity",
        "total_price",
    )

    autocomplete_fields = (
        "order",
        "variant",
    )