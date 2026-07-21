from ..models import PendingRegistration


class PendingRegistrationRepository:
    @staticmethod
    def create(
        *,
        email: str,
        first_name: str,
        last_name: str,
        password: str,
        otp_code: str,
        expires_at,
    ) -> PendingRegistration:
        return PendingRegistration.objects.create(
            email=email,
            first_name=first_name,
            last_name=last_name,
            password=password,
            otp_code=otp_code,
            expires_at=expires_at,
        )

    @staticmethod
    def update(
        *,
        pending: PendingRegistration,
        first_name: str,
        last_name: str,
        password: str,
        otp_code: str,
        expires_at,
    ) -> PendingRegistration:
        pending.first_name = first_name
        pending.last_name = last_name
        pending.password = password
        pending.otp_code = otp_code
        pending.expires_at = expires_at
        pending.attempts = 0

        pending.save(
            update_fields=[
                "first_name",
                "last_name",
                "password",
                "otp_code",
                "expires_at",
                "attempts",
                "updated_at",
            ]
        )

        return pending

    @staticmethod
    def increment_attempts(
        *,
        pending: PendingRegistration,
    ) -> PendingRegistration:
        pending.attempts += 1

        pending.save(
            update_fields=[
                "attempts",
                "updated_at",
            ]
        )

        return pending

    @staticmethod
    def delete(
        *,
        pending: PendingRegistration,
    ) -> None:
        pending.delete()