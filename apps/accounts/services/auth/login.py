from django.contrib.auth import authenticate


from ...authentication.jwt import JWT
from ...enums.login import LoginStatus

from ...selectors import UserSelector


class LoginService:
    @staticmethod
    def login(identifier: dict, password: str | None = None) -> dict:
        value = identifier["value"]
        identifier_type = identifier["type"]

        if identifier_type == "email" or identifier_type == "phone":
            user = UserSelector.get_by_email(email=value) or UserSelector.get_by_phone(
                phone=value
            )

            if not user:
                return LoginStatus.USER_NOT_FOUND

            if password is None:
                return LoginStatus.PASSWORD_REQUIRED

            user_login = authenticate(
                identifier=value,
                password=password,
            )

            if user_login is None:
                return LoginStatus.INVALID_CREDENTIALS

            tokens = JWT.create_tokens(user_login)
            return (LoginStatus.SUCCESS, {**tokens})