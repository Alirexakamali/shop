from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.accounts.services.auth.forgot_password import (
    ForgotPasswordService,
    VerifyPasswordResetService,
)

from ..serializers import (
    ForgotPasswordSerializer,
    VerifyPasswordResetSerializer,
)


class ForgotPasswordView(APIView):
    authentication_classes = ()
    permission_classes = ()

    def post(self, request):
        serializer = ForgotPasswordSerializer(
            data=request.data,
        )

        serializer.is_valid(
            raise_exception=True,
        )

        result = ForgotPasswordService.forgot_password(
            data=serializer.to_dto(),
        )

        return Response(
            {
                "status": result,
            },
            status=status.HTTP_200_OK,
        )


class VerifyPasswordResetView(APIView):
    authentication_classes = ()
    permission_classes = ()

    def post(self, request):
        serializer = VerifyPasswordResetSerializer(
            data=request.data,
        )

        serializer.is_valid(
            raise_exception=True,
        )

        result = VerifyPasswordResetService.verify(
            data=serializer.to_dto(),
        )

        return Response(
            {
                "status": result,
            },
            status=status.HTTP_200_OK,
        )