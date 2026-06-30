from django.db import models
from django.db.models import Q
from django.utils.translation import gettext_lazy as _

from common.models.base import BaseModel


class ProductImage(BaseModel):
    """
    Images for product variant with single main image rule.
    """

    variant = models.ForeignKey(
        "catalog.ProductVariant",
        on_delete=models.CASCADE,
        related_name="images",
        verbose_name=_("Variant"),
    )

    image = models.ImageField(
        upload_to="products/",
        verbose_name=_("Image"),
    )

    alt = models.CharField(
        max_length=255,
        blank=True,
        verbose_name=_("Alt text"),
    )

    is_main = models.BooleanField(
        default=False,
        verbose_name=_("Is main"),
    )

    sort_order = models.PositiveIntegerField(
        default=0,
        verbose_name=_("Sort order"),
    )

    class Meta:
        db_table = "product_images"
        ordering = ("sort_order",)
        verbose_name = _("Product Image")
        verbose_name_plural = _("Product Images")

        constraints = [
            models.UniqueConstraint(
                fields=["variant"],
                condition=Q(is_main=True),
                name="unique_main_image_per_variant",
            )
        ]