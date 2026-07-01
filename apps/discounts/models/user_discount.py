from django.db import models
from django.utils.translation import gettext_lazy as _

from common.models.base import BaseModel

class UserDiscount(BaseModel):
    user = models.ForeignKey(
        "accounts.User",
        on_delete=models.CASCADE,
        related_name="discounts",
        verbose_name=_("User"),
    )

    discount = models.ForeignKey(
        "discounts.Discount",
        on_delete=models.CASCADE,
        related_name="users",
        verbose_name=_("Discount"),
    )

    used = models.BooleanField(
        default=False,
        verbose_name=_("Used"),
    )

    used_at = models.DateTimeField(
        null=True,
        blank=True,
        verbose_name=_("Used At"),
    )

    class Meta:
        db_table = "user_discounts"
        verbose_name = _("User Discount")
        verbose_name_plural = _("User Discounts")
        constraints = [
            models.UniqueConstraint(
                fields=["user", "discount"],
                name="unique_user_discount",
            )
        ]

    def __str__(self):
        return f"{self.user} - {self.discount}"