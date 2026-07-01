from django.db import models
from django.utils.translation import gettext_lazy as _

from common.models.base import BaseModel

class Banner(BaseModel):
    """
    Website banner.
    """

    class Position(models.TextChoices):
        HOME_TOP = "home_top", _("Home Top")
        HOME_BOTTOM = "home_bottom", _("Home Bottom")
        SIDEBAR = "sidebar", _("Sidebar")

    title = models.CharField(
        max_length=255,
        verbose_name=_("Title"),
    )

    image = models.ImageField(
        upload_to="banners/",
        verbose_name=_("Image"),
    )

    url = models.URLField(
        blank=True,
        verbose_name=_("URL"),
    )

    position = models.CharField(
        max_length=30,
        choices=Position.choices,
        verbose_name=_("Position"),
    )

    is_active = models.BooleanField(
        default=True,
        verbose_name=_("Is Active"),
    )

    class Meta:
        db_table = "banners"
        verbose_name = _("Banner")
        verbose_name_plural = _("Banners")

    def __str__(self):
        return self.title