from rest_framework import serializers

from apps.accounts.dto import (
    ForgotPasswordDTO,
    VerifyPasswordResetDTO,
)


class ForgotPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField()

    def to_dto(self) -> ForgotPasswordDTO:
        return ForgotPasswordDTO(
            email=self.validated_data["email"],
        )


class VerifyPasswordResetSerializer(serializers.Serializer):
    email = serializers.EmailField()

    otp = serializers.CharField(
        max_length=6,
    )

    new_password = serializers.CharField(
        min_length=8,
        write_only=True,
    )

    def to_dto(self) -> VerifyPasswordResetDTO:
        return VerifyPasswordResetDTO(
            email=self.validated_data["email"],
            otp=self.validated_data["otp"],
            new_password=self.validated_data["new_password"],
        )