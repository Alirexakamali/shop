from django.db import models
from django.utils.translation import gettext_lazy as _

from common.models.base import BaseModel


class Payment(BaseModel):
    class Status(models.TextChoices):
        PENDING = "pending", _("Pending")
        SUCCESS = "success", _("Success")
        FAILED = "failed", _("Failed")
        CANCELED = "canceled", _("Canceled")
        REFUNDED = "refunded", _("Refunded")

    class Method(models.TextChoices):
        ONLINE = "online", _("Online")
        WALLET = "wallet", _("Wallet")
        COD = "cod", _("Cash On Delivery")

    order = models.OneToOneField(
        "orders.Order",
        on_delete=models.PROTECT,
        related_name="payment",
        verbose_name=_("Order"),
    )

    amount = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        verbose_name=_("Amount"),
    )

    method = models.CharField(
        max_length=20,
        choices=Method.choices,
        verbose_name=_("Method"),
    )

    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.PENDING,
        verbose_name=_("Status"),
    )

    authority = models.CharField(
        max_length=255,
        blank=True,
        verbose_name=_("Authority"),
    )

    transaction_id = models.CharField(
        max_length=255,
        blank=True,
        verbose_name=_("Transaction ID"),
    )

    paid_at = models.DateTimeField(
        null=True,
        blank=True,
        verbose_name=_("Paid At"),
    )

    class Meta:
        db_table = "payments"
        verbose_name = _("Payment")
        verbose_name_plural = _("Payments")

    def __str__(self):
        return str(self.order)