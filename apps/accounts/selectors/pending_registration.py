from ..models import PendingRegistration


class PendingRegistrationSelector:
    @staticmethod
    def get_by_email(*, email: str) -> PendingRegistration | None:
        return PendingRegistration.objects.filter(email=email).first()