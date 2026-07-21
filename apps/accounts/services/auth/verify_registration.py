from django.utils import timezone

from ...authentication.jwt import JWT
from ...dto import VerifyRegistrationDTO
from ...enums import VerifyRegistrationStatus
from ...repositories.pending_registration import (
    PendingRegistrationRepository,
)
from ...repositories.user import UserRepository
from ...selectors.pending_registration import (
    PendingRegistrationSelector,
)


class VerifyRegistrationService:
    MAX_ATTEMPTS = 5

    @classmethod
    def verify(
        cls,
        *,
        data: VerifyRegistrationDTO,
    ) -> VerifyRegistrationStatus:
        pending = PendingRegistrationSelector.get_by_email(
            email=data.email,
        )

        if pending is None:
            return VerifyRegistrationStatus.PENDING_REGISTRATION_NOT_FOUND

        if pending.expires_at <= timezone.now():
            PendingRegistrationRepository.delete(
                pending=pending,
            )

            return VerifyRegistrationStatus.OTP_EXPIRED

        if pending.attempts >= cls.MAX_ATTEMPTS:
            PendingRegistrationRepository.delete(
                pending=pending,
            )

            return VerifyRegistrationStatus.TOO_MANY_ATTEMPTS

        if pending.otp_code != data.otp:
            PendingRegistrationRepository.increment_attempts(
                pending=pending,
            )

            return VerifyRegistrationStatus.INVALID_OTP

        user = UserRepository.create(
            email=pending.email,
            password=pending.password,
            first_name=pending.first_name,
            last_name=pending.last_name,
        )

        PendingRegistrationRepository.delete(
            pending=pending,
        )
        tokens = JWT.create_tokens(user)

        return (VerifyRegistrationStatus.SUCCESS,{**tokens})
