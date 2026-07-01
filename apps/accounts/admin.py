from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _

from .models import Address, User


class AddressInline(admin.TabularInline):
    model = Address
    extra = 0


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    inlines = [AddressInline]

    ordering = ("-created_at",)

    list_display = (
        # "id",
        "phone",
        "email",
        "first_name",
        "last_name",
        "is_active",
        "is_staff",
        "is_superuser",
        "created_at",
    )

    list_filter = (
        "is_active",
        "is_staff",
        "is_superuser",
        "created_at",
    )

    search_fields = (
        "phone",
        "email",
        "first_name",
        "last_name",
    )

    readonly_fields = (
        "last_login",
        "created_at",
        "updated_at",
    )

    list_per_page = 25

    fieldsets = (
        (
            _("Personal Information"),
            {
                "fields": (
                    "phone",
                    "email",
                    "password",
                    "first_name",
                    "last_name",
                )
            },
        ),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
        (
            _("Important Dates"),
            {
                "fields": (
                    "last_login",
                    "created_at",
                    "updated_at",
                )
            },
        ),
    )

    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "phone",
                    "email",
                    "password1",
                    "password2",
                    "is_staff",
                    "is_superuser",
                ),
            },
        ),
    )


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "user",
        "title",
        "recipient_name",
        "city",
        "province",
        "is_default",
    )

    list_filter = (
        "province",
        "city",
        "is_default",
    )

    search_fields = (
        "user__phone",
        "user__email",
        "recipient_name",
        "postal_code",
    )

    autocomplete_fields = (
        "user",
    )

    list_per_page = 25

    ordering = (
        "-created_at",
    )