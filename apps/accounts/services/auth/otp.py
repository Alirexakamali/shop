import secrets
import string


class OTPService:
    OTP_LENGTH = 6

    @classmethod
    def generate(cls) -> str:
        return "".join(
            secrets.choice(string.digits)
            for _ in range(cls.OTP_LENGTH)
        )