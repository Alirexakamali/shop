from ..models import PasswordReset


class PasswordResetSelector:
    @staticmethod
    def get_by_user(*, user: str) -> PasswordReset | None:
        return PasswordReset.objects.filter(user=user).first()
