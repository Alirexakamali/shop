from django.db import models
from django.db.models import Q

from common.models.base import BaseModel


class ProductImage(BaseModel):
    """
    Images for product variant with single main image rule.
    """

    variant = models.ForeignKey(
        "catalog.ProductVariant",
        on_delete=models.CASCADE,
        related_name="images",
    )

    image = models.ImageField(
        upload_to="products/",
    )

    alt = models.CharField(
        max_length=255,
        blank=True,
    )

    is_main = models.BooleanField(
        default=False,
    )

    sort_order = models.PositiveIntegerField(
        default=0,
    )

    class Meta:
        db_table = "product_images"
        ordering = ("sort_order",)

        constraints = [
            models.UniqueConstraint(
                fields=["variant"],
                condition=Q(is_main=True),
                name="unique_main_image_per_variant",
            )
        ]
