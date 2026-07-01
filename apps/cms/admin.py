from django.contrib import admin

from .models import Banner, Page


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "slug",
        "is_published",
    )

    list_editable = (
        "is_published",
    )

    search_fields = (
        "title",
        "slug",
    )


@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "position",
        "is_active",
    )

    list_filter = (
        "position",
        "is_active",
    )

    list_editable = (
        "is_active",
    )

    search_fields = (
        "title",
    )