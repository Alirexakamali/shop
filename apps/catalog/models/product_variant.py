from django.db import models
from django.utils.translation import gettext_lazy as _

from common.models.base import BaseModel


class ProductVariant(BaseModel):
    """
    Sellable unit of a product (SKU level).
    """

    product = models.ForeignKey(
        "catalog.Product",
        on_delete=models.CASCADE,
        related_name="variants",
        verbose_name=_("Product"),
    )

    sku = models.CharField(
        max_length=100,
        unique=True,
        verbose_name=_("SKU"),
    )

    barcode = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        unique=True,
        verbose_name=_("Barcode"),
    )

    price = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        verbose_name=_("Price"),
    )

    discount_price = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        null=True,
        blank=True,
        verbose_name=_("Discount price"),
    )

    weight = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True,
        verbose_name=_("Weight"),
    )

    is_active = models.BooleanField(
        default=True,
        verbose_name=_("Is active"),
    )

    class Meta:
        db_table = "product_variants"
        verbose_name = _("Product Variant")
        verbose_name_plural = _("Product Variants")
        indexes = [
            models.Index(fields=["sku"]),
            models.Index(fields=["product", "is_active"]),
        ]

    def __str__(self):
        return f"{self.product.name} - {self.sku}"