from django.db import models

from common.models.base import BaseModel


class ProductVariant(BaseModel):
    """
    Sellable unit of a product (SKU level).
    """

    product = models.ForeignKey(
        "catalog.Product",
        on_delete=models.CASCADE,
        related_name="variants",
    )

    sku = models.CharField(
        max_length=100,
        unique=True,
    )

    barcode = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        unique=True,
    )

    price = models.DecimalField(
        max_digits=12,
        decimal_places=2,
    )

    discount_price = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        null=True,
        blank=True,
    )

    weight = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True,
    )

    is_active = models.BooleanField(
        default=True,
    )

    class Meta:
        db_table = "product_variants"
        indexes = [
            models.Index(fields=["sku"]),
            models.Index(fields=["product", "is_active"]),
        ]

    def __str__(self):
        return f"{self.product.name} - {self.sku}"