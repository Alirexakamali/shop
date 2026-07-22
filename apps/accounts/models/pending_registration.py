from django.db import models

from common.models.base import BaseModel

class PendingRegistration(BaseModel):
    
    email = models.EmailField(unique=True)

    first_name = models.CharField(max_length=150)

    last_name = models.CharField(max_length=150)

    password = models.CharField(max_length=128)

    otp_code = models.CharField(max_length=6)

    expires_at = models.DateTimeField()

    attempts = models.PositiveSmallIntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)