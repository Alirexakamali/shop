from django.db import models
from django.utils.translation import gettext_lazy as _

from common.models.base import BaseModel


class Brand(BaseModel):
    """
    Product brand (e.g. Apple, Samsung).
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

    logo = models.ImageField(
        upload_to="brands/",
        blank=True,
        null=True,
        verbose_name=_("Logo"),
    )

    is_active = models.BooleanField(
        default=True,
        verbose_name=_("Is active"),
    )

    class Meta:
        db_table = "brands"
        ordering = ("name",)
        verbose_name = _("Brand")
        verbose_name_plural = _("Brands")

    def __str__(self):
        return self.name