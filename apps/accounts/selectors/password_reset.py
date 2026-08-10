from ..models import PasswordReset


class PasswordResetSelector:
    @staticmethod
    def get_by_user(*, user: str) -> PasswordReset | None:
        try:
            return PasswordReset.objects.get(user=user)
        except PasswordReset.DoesNotExist:
            return None

        # NOTE :
        # If you accidentally create two records with the same email, get() will throw a MultipleObjectsReturned error and you will quickly notice the bug.
        # first() in this case will silently return the first record and may hide the bug.

        # return PasswordReset.objects.filter(user=user).first()
