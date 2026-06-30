from django.db import models

from common.models.base import BaseModel


class ProductVariantAttribute(BaseModel):
    """
    Links product variant to attribute values.
    """

    variant = models.ForeignKey(
        "catalog.ProductVariant",
        on_delete=models.CASCADE,
        related_name="attributes",
    )

    attribute = models.ForeignKey(
        "catalog.Attribute",
        on_delete=models.CASCADE,
    )

    value = models.ForeignKey(
        "catalog.AttributeValue",
        on_delete=models.CASCADE,
    )

    class Meta:
        db_table = "variant_attributes"
        unique_together = ("variant", "attribute")

    def __str__(self):
        return f"{self.variant} - {self.attribute.name}: {self.value.value}"