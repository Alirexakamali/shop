from uuid import UUID

from ..models import User


class UserSelector:
    @staticmethod
    def exists_by_email(*, email: str) -> bool:
        return User.objects.filter(email=email).exists()

    @staticmethod
    def get_by_email(*, email: str) -> User | None:
        return User.objects.filter(email=email).first()

    @staticmethod
    def exists_by_phone(*, phone: str) -> bool:
        return User.objects.filter(phone=phone).exists()

    @staticmethod
    def get_by_phone(*, phone: str) -> User | None:
        return User.objects.filter(phone=phone).first()

    @staticmethod
    def exists_by_id(*, user_id: UUID) -> bool:
        return User.objects.filter(id=user_id).exists()

    @staticmethod
    def get_by_id(*, user_id) -> User | None:
        return User.objects.filter(id=user_id).first()
