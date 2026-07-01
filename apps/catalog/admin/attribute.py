from django.contrib import admin

from ..models import Attribute

from ..inlines import AttributeValueInline


@admin.register(Attribute)
class AttributeAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
    )

    search_fields = ("name",)

    inlines = [
        AttributeValueInline,
    ]
