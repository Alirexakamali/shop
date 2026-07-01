from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.db.models import Q
from django.utils.translation import gettext_lazy as _

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
        verbose_name=_("Email"),
    )

    phone = models.CharField(
        max_length=11,
        unique=True,
        null=True,
        blank=True,
        db_index=True,
        verbose_name=_("Phone"),
    )

    first_name = models.CharField(
        max_length=100,
        blank=True,
        verbose_name=_("First name"),
    )

    last_name = models.CharField(
        max_length=100,
        blank=True,
        verbose_name=_("Last name"),
    )

    avatar = models.ImageField(
        upload_to="users/avatars/",
        blank=True,
        null=True,
        verbose_name=_("Avatar"),
    )

    is_active = models.BooleanField(
        default=True,
        verbose_name=_("Is active"),
    )

    is_staff = models.BooleanField(
        default=False,
        verbose_name=_("Is staff"),
    )

    date_joined = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_("Date joined"),
    )

    objects = UserManager()

    USERNAME_FIELD = "phone"
    # USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        db_table = "users"
        verbose_name = _("User")
        verbose_name_plural = _("Users")

        # NOTE : This restriction is used when both are mandatory (phone , email).
        # constraints = [
        #     models.CheckConstraint(
        #         condition=Q(phone__isnull=False) | Q(email__isnull=False),
        #         name="user_phone_or_email_required",
        #     )
        # ]

    def __str__(self):
        return self.email or self.phone