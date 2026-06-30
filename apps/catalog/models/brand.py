from django.db import models

from common.models.base import BaseModel


class Brand(BaseModel):
    """
    Product brand (e.g. Apple, Samsung).
    """

    name = models.CharField(
        max_length=255,
        unique=True,
    )

    slug = models.SlugField(
        max_length=255,
        unique=True,
    )

    logo = models.ImageField(
        upload_to="brands/",
        blank=True,
        null=True,
    )

    is_active = models.BooleanField(
        default=True,
    )

    class Meta:
        db_table = "brands"
        ordering = ("name",)

    def __str__(self):
        return self.name