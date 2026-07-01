from django.db import models
from django.utils.translation import gettext_lazy as _

from common.models.base import BaseModel

class CartItem(BaseModel):
    """
    Item in shopping cart.
    """

    cart = models.ForeignKey(
        "cart.Cart",
        on_delete=models.CASCADE,
        related_name="items",
        verbose_name=_("Cart"),
    )

    variant = models.ForeignKey(
        "catalog.ProductVariant",
        on_delete=models.CASCADE,
        related_name="cart_items",
        verbose_name=_("Variant"),
    )

    quantity = models.PositiveIntegerField(
        default=1,
        verbose_name=_("Quantity"),
    )

    class Meta:
        db_table = "cart_items"
        verbose_name = _("Cart Item")
        verbose_name_plural = _("Cart Items")
        constraints = [
            models.UniqueConstraint(
                fields=["cart", "variant"],
                name="unique_variant_per_cart",
            ),
        ]

    def __str__(self):
        return f"{self.variant} × {self.quantity}"