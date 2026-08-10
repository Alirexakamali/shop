from datetime import timedelta

from django.utils import timezone

from ...dto import ForgotPasswordDTO, VerifyPasswordResetDTO
from ...enums import ForgotPasswordStatus, VerifyPasswordResetStatus
from ...repositories import PasswordResetRepository, UserRepository
from ...selectors import PasswordResetSelector, UserSelector


# from ..email.sender import EmailService
from ...tasks import send_register_otp
from .otp import OTPService


class ForgotPasswordService:
    OTP_EXPIRE_MINUTES = 2

    @classmethod
    def forgot_password(
        cls,
        *,
        data: ForgotPasswordDTO,
    ) -> ForgotPasswordStatus:
        user = UserSelector.get_by_email(
            email=data.email,
        )

        if user is None:
            return ForgotPasswordStatus.USER_NOT_FOUND

        password_reset = PasswordResetSelector.get_by_user(
            user=user,
        )

        otp = OTPService.generate()

        expires_at = timezone.now() + timedelta(
            minutes=cls.OTP_EXPIRE_MINUTES,
        )

        if password_reset:
            PasswordResetRepository.update(
                password_reset=password_reset,
                otp_code=otp,
                expires_at=expires_at,
            )
        else:
            PasswordResetRepository.create(
                user=user,
                otp_code=otp,
                expires_at=expires_at,
            )
        # NOTE : To avoid problems on a scale of 50,000 or more, we document the email with Celery.
        # EmailService.send_verification_code(
        #     email=user.email,
        #     otp=otp,
        # )
        
        send_register_otp.delay(
            email=user.email,
            otp=otp,
        )

        return ForgotPasswordStatus.OTP_SENT


class VerifyPasswordResetService:
    MAX_ATTEMPTS = 5

    @classmethod
    def verify(
        cls,
        *,
        data: VerifyPasswordResetDTO,
    ) -> VerifyPasswordResetStatus:
        user = UserSelector.get_by_email(
            email=data.email,
        )

        if user is None:
            return VerifyPasswordResetStatus.USER_NOT_FOUND

        password_reset = PasswordResetSelector.get_by_user(
            user=user,
        )

        if password_reset is None:
            return VerifyPasswordResetStatus.PASSWORD_RESET_NOT_FOUND

        if password_reset.expires_at <= timezone.now():
            PasswordResetRepository.delete(
                password_reset=password_reset,
            )

            return VerifyPasswordResetStatus.OTP_EXPIRED

        if password_reset.attempts >= cls.MAX_ATTEMPTS:
            PasswordResetRepository.delete(
                password_reset=password_reset,
            )

            return VerifyPasswordResetStatus.TOO_MANY_ATTEMPTS

        if password_reset.otp_code != data.otp:
            PasswordResetRepository.increment_attempts(
                password_reset=password_reset,
            )

            return VerifyPasswordResetStatus.INVALID_OTP

        UserRepository.change_password(
            user=user,
            password=data.new_password,
        )

        PasswordResetRepository.delete(
            password_reset=password_reset,
        )

        return VerifyPasswordResetStatus.SUCCESS
