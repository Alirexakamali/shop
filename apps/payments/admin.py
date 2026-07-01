from django.contrib import admin

from .models import Payment


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "order",
        "amount",
        "method",
        "status",
        "paid_at",
    )

    list_filter = (
        "status",
        "method",
    )

    search_fields = (
        "authority",
        "transaction_id",
        "order__id",
    )

    autocomplete_fields = (
        "order",
    )

    ordering = (
        "-created_at",
    )