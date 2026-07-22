from ..models import PasswordReset, User


class PasswordResetRepository:
    @staticmethod
    def create(
        *,
        user: User,
        otp_code: str,
        expires_at,
    ) -> PasswordReset:
        return PasswordReset.objects.create(
            user=user,
            otp_code=otp_code,
            expires_at=expires_at,
        )

    @staticmethod
    def update(
        *,
        password_reset: PasswordReset,
        otp_code: str,
        expires_at,
    ) -> PasswordReset:
        password_reset.otp_code = otp_code
        password_reset.expires_at = expires_at
        password_reset.attempts = 0

        password_reset.save(
            update_fields=[
                "otp_code",
                "expires_at",
                "attempts",
                "updated_at",
            ]
        )

        return password_reset

    @staticmethod
    def increment_attempts(
        *,
        password_reset: PasswordReset,
    ) -> PasswordReset:
        password_reset.attempts += 1

        password_reset.save(
            update_fields=[
                "attempts",
                "updated_at",
            ]
        )

        return password_reset

    @staticmethod
    def delete(
        *,
        password_reset: PasswordReset,
    ) -> None:
        password_reset.delete()
        
        