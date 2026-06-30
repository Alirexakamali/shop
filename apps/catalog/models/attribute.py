from django.db import models
from django.utils.translation import gettext_lazy as _

from common.models.base import BaseModel


class Attribute(BaseModel):
    """
    Defines a product attribute type (e.g. Color, Size, RAM).
    """

    name = models.CharField(
        max_length=255,
        unique=True,
        verbose_name=_("Name"),
    )

    slug = models.SlugField(
        max_length=255,
        unique=True,
        verbose_name=_("Slug"),
    )

    class Meta:
        db_table = "attributes"
        ordering = ("name",)
        verbose_name = _("Attribute")
        verbose_name_plural = _("Attributes")

    def __str__(self):
        return self.name