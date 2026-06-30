from django.db import models
from django.utils.translation import gettext_lazy as _

from common.models.base import BaseModel


class Product(BaseModel):
    """
    Main product entity (not sellable directly).
    """

    category = models.ForeignKey(
        "catalog.Category",
        on_delete=models.PROTECT,
        related_name="products",
        verbose_name=_("Category"),
    )

    brand = models.ForeignKey(
        "catalog.Brand",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="products",
        verbose_name=_("Brand"),
    )

    name = models.CharField(
        max_length=255,
        verbose_name=_("Name"),
    )

    slug = models.SlugField(
        max_length=255,
        unique=True,
        verbose_name=_("Slug"),
    )

    description = models.TextField(
        blank=True,
        verbose_name=_("Description"),
    )

    short_description = models.CharField(
        max_length=500,
        blank=True,
        verbose_name=_("Short description"),
    )

    is_active = models.BooleanField(
        default=True,
        verbose_name=_("Is active"),
    )

    class Meta:
        db_table = "products"
        verbose_name = _("Product")
        verbose_name_plural = _("Products")
        indexes = [
            models.Index(fields=["category", "is_active"]),
        ]
        ordering = ("-created_at",)

    def __str__(self):
        return self.name