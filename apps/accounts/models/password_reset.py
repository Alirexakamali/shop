from django.db import models

from .user import User
from common.models.base import BaseModel


class PasswordReset(BaseModel):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="password_reset_requests",
    )

    otp_code = models.CharField(max_length=6)

    expires_at = models.DateTimeField()

    attempts = models.PositiveSmallIntegerField(default=0)
