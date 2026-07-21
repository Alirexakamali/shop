from ..models import User


class UserRepository:
    @staticmethod
    def create(
        *,
        email: str,
        password: str,
        first_name: str,
        last_name: str,
    ) -> User:
        return User.objects.create(
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name,
        )