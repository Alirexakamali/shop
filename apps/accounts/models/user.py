from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.db.models import Q

from common.models.base import BaseModel

from ..managers import UserManager


class User(BaseModel, AbstractBaseUser, PermissionsMixin):
    """
    Custom user model.
    """

    email = models.EmailField(
        unique=True,
        null=True,
        blank=True,
        db_index=True,
    )

    phone = models.CharField(
        max_length=11,
        unique=True,
        null=True,
        blank=True,
        db_index=True,
    )

    first_name = models.CharField(
        max_length=100,
        blank=True,
    )

    last_name = models.CharField(
        max_length=100,
        blank=True,
    )

    avatar = models.ImageField(
        upload_to="users/avatars/",
        blank=True,
        null=True,
    )

    is_active = models.BooleanField(
        default=True,
    )

    is_staff = models.BooleanField(
        default=False,
    )

    date_joined = models.DateTimeField(
        auto_now_add=True,
    )

    objects = UserManager()

    USERNAME_FIELD = "phone"
    REQUIRED_FIELDS = []

    class Meta:
        db_table = "users"
 
        # NOTE : This restriction is used when both are mandatory (phone , email).
        # constraints = [
        #     models.CheckConstraint(
        #         condition=Q(phone__isnull=False) | Q(email__isnull=False),
        #         name="user_phone_or_email_required",
        #     )
        # ]


    def __str__(self):
        return self.email or self.phone
