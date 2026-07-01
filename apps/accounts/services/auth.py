from ..models import User


class AuthService:
    @staticmethod
    def login(identifier: dict) -> dict:
        value = identifier["value"]
        identifier_type = identifier["type"]

        if identifier_type == "email":
            user = User.objects.filter(email=value).first()

            if not user:
                return {
                    "status": "USER_NOT_FOUND",
                }

            return {
                "status": "PASSWORD_REQUIRED",
                "user_id": user.id,
            }

        user = User.objects.filter(phone=value).first()

        if user:
            return {
                "status": "SEND_OTP",
                "user_id": user.id,
            }

        return {
            "status": "REGISTER_WITH_OTP",
        }