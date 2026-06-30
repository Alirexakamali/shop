from django.db import models
from django.utils.translation import gettext_lazy as _

from common.models.base import BaseModel


class ProductVariantAttribute(BaseModel):
    """
    Links product variant to attribute values.
    """

    variant = models.ForeignKey(
        "catalog.ProductVariant",
        on_delete=models.CASCADE,
        related_name="attributes",
        verbose_name=_("Variant"),
    )

    attribute = models.ForeignKey(
        "catalog.Attribute",
        on_delete=models.CASCADE,
        verbose_name=_("Attribute"),
    )

    value = models.ForeignKey(
        "catalog.AttributeValue",
        on_delete=models.CASCADE,
        verbose_name=_("Value"),
    )

    class Meta:
        db_table = "variant_attributes"
        unique_together = ("variant", "attribute")
        verbose_name = _("Product Variant Attribute")
        verbose_name_plural = _("Product Variant Attributes")

    def __str__(self):
        return f"{self.variant} - {self.attribute.name}: {self.value.value}"