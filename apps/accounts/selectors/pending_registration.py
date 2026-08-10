from ..models import PendingRegistration


class PendingRegistrationSelector:
    @staticmethod
    def get_by_email(*, email: str) -> PendingRegistration | None:
        try:
            return PendingRegistration.objects.get(email=email)
        except PendingRegistration.DoesNotExist:
            return None

        # NOTE :
        # If you accidentally create two records with the same email, get() will throw a MultipleObjectsReturned error and you will quickly notice the bug.
        # first() in this case will silently return the first record and may hide the bug.

        # return PendingRegistration.objects.filter(email=email).first()
