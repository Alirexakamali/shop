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
            user = (
                UserSelector.get_by_email(email=value)
                or UserSelector.get_by_phone(phone=value)
            )

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
            tokens = JWT.create_tokens(user_login)
            return {
                "status": LoginStatus.SUCCESS,
                **tokens,
            }

        # user = User.objects.filter(phone=value).first()

        # if user:
        #     return {
        #         "status": LoginStatus.SEND_OTP,
        #         "user_id": user.id,
        #     }

        # return {
        #     "status": LoginStatus.REGISTER_WITH_OTP,
        # }
