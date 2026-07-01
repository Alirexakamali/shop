from django.contrib import admin

from ..models import AttributeValue

@admin.register(AttributeValue)
class AttributeValueAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "attribute",
        "value",
    )

    list_filter = (
        "attribute",
    )

    search_fields = (
        "value",
    )

    autocomplete_fields = (
        "attribute",
    )