from datetime import timedelta

from django.contrib.auth.hashers import make_password
from django.utils import timezone

from ...dto.register import RegisterDTO
from ...enums.register import RegisterStatus
from ...repositories.pending_registration import PendingRegistrationRepository
from ...selectors.pending_registration import PendingRegistrationSelector
from ...selectors.user import UserSelector

# from ..email.sender import EmailService
from ...tasks import send_register_otp
from .otp import OTPService


class RegisterService:
    OTP_EXPIRE_MINUTES = 2

    @classmethod
    def register(cls, *, data: RegisterDTO) -> RegisterStatus:
        if UserSelector.exists_by_email(email=data.email):
            return RegisterStatus.USER_ALREADY_EXISTS

        pending = PendingRegistrationSelector.get_by_email(
            email=data.email,
        )

        otp = OTPService.generate()

        expires_at = timezone.now() + timedelta(
            minutes=cls.OTP_EXPIRE_MINUTES,
        )

        hashed_password = make_password(data.password)

        if pending:
            PendingRegistrationRepository.update(
                pending=pending,
                first_name=data.first_name,
                last_name=data.last_name,
                password=hashed_password,
                otp_code=otp,
                expires_at=expires_at,
            )
        else:
            PendingRegistrationRepository.create(
                email=data.email,
                first_name=data.first_name,
                last_name=data.last_name,
                password=hashed_password,
                otp_code=otp,
                expires_at=expires_at,
            )
        # NOTE : To avoid problems on a scale of 50,000 or more, we document the email with Celery.
        # EmailService.send_verification_code(
        #     email=data.email,
        #     otp=otp,
        # )
        send_register_otp.delay(
            email=data.email,
            otp=otp,
        )

        return RegisterStatus.OTP_SENT
