from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.accounts.services.auth.register import RegisterService
from apps.accounts.services.auth.verify_registration import VerifyRegistrationService

from ..serializers import RegisterSerializer, VerifyRegistrationSerializer


class RegisterView(APIView):
    authentication_classes = ()
    permission_classes = ()

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        result = RegisterService.register(
            data=serializer.to_dto(),
        )

        return Response({"status": result}, status=status.HTTP_200_OK)


class VerifyRegistrationView(APIView):
    authentication_classes = []
    permission_classes = []

    def post(self, request):
        serializer = VerifyRegistrationSerializer(
            data=request.data,
        )

        serializer.is_valid(
            raise_exception=True,
        )

        result = VerifyRegistrationService.verify(
            data=serializer.to_dto(),
        )

        return Response(
            {
                "status": result,
            },
            status=status.HTTP_200_OK,
        )
