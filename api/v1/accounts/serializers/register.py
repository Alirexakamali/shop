from rest_framework import serializers

from apps.accounts.dto.register import RegisterDTO


class RegisterSerializer(serializers.Serializer):
    first_name = serializers.CharField(max_length=100)
    last_name = serializers.CharField(max_length=100)
    email = serializers.EmailField(max_length=255)
    password = serializers.CharField(
        min_length=8,
        write_only=True,
    )

    def to_dto(self) -> RegisterDTO:
        return RegisterDTO(
            first_name=self.validated_data["first_name"],
            last_name=self.validated_data["last_name"],
            email=self.validated_data["email"],
            password=self.validated_data["password"],
        )