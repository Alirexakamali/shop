from django.core.validators import validate_email
from rest_framework import serializers

from apps.accounts.normalizers import NormalizerPhone


class LoginSerializer(serializers.Serializer):
    identifier = serializers.CharField(max_length=255)
    password = serializers.CharField(
        required=False,
        allow_blank=True,
        write_only=True,
    )

    def validate_identifier(self, value):
        value = value.strip()

        try:
            validate_email(value)
            return {
                "type": "email",
                "value": value.lower(),
            }
        except Exception:
            pass

        try:
            NormalizerPhone.normalize_phone(value)
            return {
                "type": "phone",
                "value": value,
            }
        except Exception:
            pass

        raise serializers.ValidationError(
            "Enter a valid email or phone number."
        )