from django.db import models

from common.models.base import BaseModel


class AttributeValue(BaseModel):
    """
    Values for an attribute (e.g. Red, Blue, 128GB).
    """

    attribute = models.ForeignKey(
        "catalog.Attribute",
        on_delete=models.CASCADE,
        related_name="values",
    )

    value = models.CharField(
        max_length=255,
    )

    slug = models.SlugField(
        max_length=255,
    )

    class Meta:
        db_table = "attribute_values"
        unique_together = ("attribute", "value")
        ordering = ("value",)

    def __str__(self):
        return f"{self.attribute.name}: {self.value}"