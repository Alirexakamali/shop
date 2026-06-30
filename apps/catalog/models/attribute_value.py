from django.db import models
from django.utils.translation import gettext_lazy as _
from common.models.base import BaseModel


class AttributeValue(BaseModel):
    """
    Values for an attribute (e.g. Red, Blue, 128GB).
    """

    attribute = models.ForeignKey(
        "catalog.Attribute",
        on_delete=models.CASCADE,
        related_name="values",
        verbose_name=_("Attribute"),
    )

    value = models.CharField(
        max_length=255,
        verbose_name=_("Value"),
    )

    slug = models.SlugField(
        max_length=255,
        verbose_name=_("Slug"),
    )

    class Meta:
        db_table = "attribute_values"
        unique_together = ("attribute", "value")
        ordering = ("value",)
        verbose_name = _("Attribute Value")
        verbose_name_plural = _("Attribute Values")

    def __str__(self):
        return f"{self.attribute.name}: {self.value}"