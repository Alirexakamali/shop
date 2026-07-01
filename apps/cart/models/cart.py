from django.db import models
from django.utils.translation import gettext_lazy as _

from common.models.base import BaseModel


class Cart(BaseModel):
    """
    Shopping cart.
    """

    user = models.OneToOneField(
        "accounts.User",
        on_delete=models.CASCADE,
        related_name="cart",
        verbose_name=_("User"),
    )

    class Meta:
        db_table = "carts"
        verbose_name = _("Cart")
        verbose_name_plural = _("Carts")

    def __str__(self):
        return str(self.user)