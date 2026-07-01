from django.db import models
from django.utils.translation import gettext_lazy as _

from common.models.base import BaseModel


class Review(BaseModel):
    """
    Product review.
    """

    user = models.ForeignKey(
        "accounts.User",
        on_delete=models.CASCADE,
        related_name="reviews",
        verbose_name=_("User"),
    )

    product = models.ForeignKey(
        "catalog.Product",
        on_delete=models.CASCADE,
        related_name="reviews",
        verbose_name=_("Product"),
    )

    rating = models.PositiveSmallIntegerField(
        verbose_name=_("Rating"),
    )

    title = models.CharField(
        max_length=255,
        blank=True,
        verbose_name=_("Title"),
    )

    comment = models.TextField(
        verbose_name=_("Comment"),
    )

    is_approved = models.BooleanField(
        default=False,
        verbose_name=_("Is Approved"),
    )

    class Meta:
        db_table = "reviews"
        verbose_name = _("Review")
        verbose_name_plural = _("Reviews")
        constraints = [
            models.UniqueConstraint(
                fields=["user", "product"],
                name="unique_review_per_user",
            )
        ]

    def __str__(self):
        return f"{self.product} ({self.rating})"