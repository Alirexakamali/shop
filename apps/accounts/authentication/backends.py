from django.contrib.auth.backends import BaseBackend

from ..models import User


class EmailOrPhoneBackend(BaseBackend):
    def authenticate(
        self,
        request,
        identifier=None,
        username=None,
        password=None,
        **kwargs,
    ):
        identifier = identifier or username

        if not identifier or not password:
            return None

        user = User.objects.filter(email=identifier).first()

        if user is None:
            user = User.objects.filter(phone=identifier).first()

        if user and user.check_password(password):
            return user

        return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
