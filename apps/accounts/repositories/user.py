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

    @staticmethod
    def change_password(
        *,
        user: User,
        password: str,
    ) -> User:
        user.set_password(password)

        user.save(
            update_fields=[
                "password",
            ]
        )

        return user
