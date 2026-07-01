from django.contrib import admin

from .models import Discount, UserDiscount


class UserDiscountInline(admin.TabularInline):
    model = UserDiscount
    extra = 0


@admin.register(Discount)
class DiscountAdmin(admin.ModelAdmin):
    inlines = [UserDiscountInline]

    list_display = (
        "code",
        "discount_type",
        "value",
        "used_count",
        "is_active",
    )

    list_filter = (
        "discount_type",
        "is_active",
    )

    search_fields = (
        "code",
    )


@admin.register(UserDiscount)
class UserDiscountAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "discount",
        "used",
        "used_at",
    )

    autocomplete_fields = (
        "user",
        "discount",
    )