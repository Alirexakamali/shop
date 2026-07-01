from django.db import models
from django.utils.translation import gettext_lazy as _

from common.models.base import BaseModel


class Shipment(BaseModel):
    """
    Shipment information.
    """

    class Status(models.TextChoices):
        PENDING = "pending", _("Pending")
        PACKING = "packing", _("Packing")
        SHIPPED = "shipped", _("Shipped")
        DELIVERED = "delivered", _("Delivered")
        RETURNED = "returned", _("Returned")

    order = models.OneToOneField(
        "orders.Order",
        on_delete=models.CASCADE,
        related_name="shipment",
        verbose_name=_("Order"),
    )

    shipping_method = models.ForeignKey(
        "shipping.ShippingMethod",
        on_delete=models.PROTECT,
        related_name="shipments",
        verbose_name=_("Shipping Method"),
    )

    tracking_code = models.CharField(
        max_length=100,
        blank=True,
        verbose_name=_("Tracking Code"),
    )

    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.PENDING,
        verbose_name=_("Status"),
    )

    shipped_at = models.DateTimeField(
        null=True,
        blank=True,
        verbose_name=_("Shipped At"),
    )

    delivered_at = models.DateTimeField(
        null=True,
        blank=True,
        verbose_name=_("Delivered At"),
    )

    class Meta:
        db_table = "shipments"
        verbose_name = _("Shipment")
        verbose_name_plural = _("Shipments")

    def __str__(self):
        return f"Shipment #{self.pk}"
