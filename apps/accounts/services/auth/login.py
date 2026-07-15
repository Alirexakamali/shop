from django.contrib.auth import authenticate

from ...models import User

from .jwt import JWTService
from ...enums.login import LoginStatus


class LoginService:
    @staticmethod
    def login(identifier: dict, password: str | None = None) -> dict:
        value = identifier["value"]
        identifier_type = identifier["type"]

        if identifier_type == "email":
            user = User.objects.filter(email=value).first()

            if not user:
                return {
                    "status": LoginStatus.USER_NOT_FOUND,
                }

            if password is None:
                return {
                    "status": LoginStatus.PASSWORD_REQUIRED,
                }

            user_login = authenticate(
                identifier=value,
                password=password,
            )

            if user_login is None:
                return {
                    "status": LoginStatus.INVALID_CREDENTIALS,
                }
            tokens = JWTService.create_tokens(user_login)
            return {
                "status": LoginStatus.INVALID_CREDENTIALS,
                **tokens,
            }

        user = User.objects.filter(phone=value).first()

        if user:
            return {
                "status": LoginStatus.SEND_OTP,
                "user_id": user.id,
            }

        return {
            "status": LoginStatus.REGISTER_WITH_OTP,
        }
