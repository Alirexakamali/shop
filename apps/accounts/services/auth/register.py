from django.contrib.auth.hashers import make_password

from ...dto.register import RegisterDTO
from ...enums.register import RegisterStatus
from ...selectors import PendingRegistrationSelector, UserSelector
from ...services.auth.otp import OTPService


class RegisterService:
    @staticmethod
    def register(*, data: RegisterDTO) -> RegisterStatus:
        if UserSelector.exists_by_email(email=data.email):
            return RegisterStatus.USER_ALREADY_EXISTS

        pending = PendingRegistrationSelector.get_by_email(
            email=data.email,
        )

        otp = OTPService.generate()

        hashed_password = make_password(data.password)

        if pending:
            # update pending registration
            ...

        else:
            # create pending registration
            ...

        return {"status": RegisterStatus.OTP_SENT}
