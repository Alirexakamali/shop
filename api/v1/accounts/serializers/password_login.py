from django.contrib.auth import authenticate

from rest_framework import serializers


class PasswordLoginSerializer(serializers.Serializer):
    identifier = serializers.CharField(max_length=255)
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        user = authenticate(
            identifier=attrs["identifier"].strip(),
            password=attrs["password"],
        )

        if user is None:
            raise serializers.ValidationError(
                "Invalid credentials."
            )

        attrs["user"] = user
        return attrs