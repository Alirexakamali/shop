from django.db import models

from common.models.base import BaseModel


class Product(BaseModel):
    """
    Main product entity (not sellable directly).
    """

    category = models.ForeignKey(
        "catalog.Category",
        on_delete=models.PROTECT,
        related_name="products",
    )

    brand = models.ForeignKey(
        "catalog.Brand",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="products",
    )

    name = models.CharField(
        max_length=255,
    )

    slug = models.SlugField(
        max_length=255,
        unique=True,
    )

    description = models.TextField(
        blank=True,
    )

    short_description = models.CharField(
        max_length=500,
        blank=True,
    )

    is_active = models.BooleanField(
        default=True,
    )

    class Meta:
        db_table = "products"
        indexes = [
            models.Index(fields=["category", "is_active"]),
        ]
        ordering = ("-created_at",)

    def __str__(self):
        return self.name