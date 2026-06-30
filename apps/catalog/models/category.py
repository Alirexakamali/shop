from django.db import models
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _

from common.models.base import BaseModel


class Category(BaseModel):
    """
    Product category.
    """

    parent = models.ForeignKey(
        "self",
        on_delete=models.CASCADE,
        related_name="children",
        null=True,
        blank=True,
        verbose_name=_("Parent"),
    )

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

    description = models.TextField(
        blank=True,
        verbose_name=_("Description"),
    )

    image = models.ImageField(
        upload_to="categories/",
        blank=True,
        null=True,
        verbose_name=_("Image"),
    )

    is_active = models.BooleanField(
        default=True,
        verbose_name=_("Is active"),
    )

    sort_order = models.PositiveIntegerField(
        default=0,
        verbose_name=_("Sort order"),
    )

    class Meta:
        db_table = "categories"
        ordering = ("sort_order", "name")
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)

        super().save(*args, **kwargs)

    def __str__(self):
        return self.name