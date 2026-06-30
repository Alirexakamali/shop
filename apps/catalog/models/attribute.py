from django.db import models

from common.models.base import BaseModel


class Attribute(BaseModel):
    """
    Defines a product attribute type (e.g. Color, Size, RAM).
    """

    name = models.CharField(
        max_length=255,
        unique=True,
    )

    slug = models.SlugField(
        max_length=255,
        unique=True,
    )

    class Meta:
        db_table = "attributes"
        ordering = ("name",)

    def __str__(self):
        return self.name