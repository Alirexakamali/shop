from django.db import models
from django.utils.translation import gettext_lazy as _

from common.models.base import BaseModel


class Page(BaseModel):
    """
    Static website page.
    """

    title = models.CharField(
        max_length=255,
        verbose_name=_("Title"),
    )

    slug = models.SlugField(
        unique=True,
        verbose_name=_("Slug"),
    )

    content = models.TextField(
        verbose_name=_("Content"),
    )

    is_published = models.BooleanField(
        default=True,
        verbose_name=_("Is Published"),
    )

    class Meta:
        db_table = "pages"
        verbose_name = _("Page")
        verbose_name_plural = _("Pages")

    def __str__(self):
        return self.title


