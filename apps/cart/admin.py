from django.contrib import admin

from .models import Cart, CartItem


class CartItemInline(admin.TabularInline):
    model = CartItem
    extra = 0


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    inlines = [CartItemInline]

    list_display = (
        "id",
        "user",
        "created_at",
    )

    autocomplete_fields = (
        "user",
    )

    search_fields = (
        "user__phone",
        "user__email",
    )


@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = (
        "cart",
        "variant",
        "quantity",
    )

    autocomplete_fields = (
        "cart",
        "variant",
    )