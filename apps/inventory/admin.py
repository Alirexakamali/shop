from django.contrib import admin

from .models import Inventory, StockMovement


class StockMovementInline(admin.TabularInline):
    model = StockMovement
    extra = 0
    readonly_fields = (
        "movement_type",
        "quantity",
        "description",
        "created_at",
    )

    can_delete = False


@admin.register(Inventory)
class InventoryAdmin(admin.ModelAdmin):
    inlines = [StockMovementInline]

    list_display = (
        "variant",
        "quantity",
        "reserved_quantity",
        "available_quantity",
        "low_stock_threshold",
    )

    autocomplete_fields = ("variant",)

    search_fields = (
        "variant__sku",
        "variant__product__name",
    )

    list_select_related = ("variant",)


@admin.register(StockMovement)
class StockMovementAdmin(admin.ModelAdmin):
    list_display = (
        "inventory",
        "movement_type",
        "quantity",
        "created_at",
    )

    autocomplete_fields = ("inventory",)

    list_filter = ("movement_type",)

    search_fields = ("inventory__variant__sku",)
