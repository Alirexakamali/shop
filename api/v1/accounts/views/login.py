from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.accounts.services.auth.login import LoginService

from ..serializers import LoginSerializer


class LoginView(APIView):
    authentication_classes = ()
    permission_classes = ()

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        result = LoginService.login(
            identifier=serializer.validated_data.get("identifier"),
            password=serializer.validated_data.get("password") or None,
        )

        return Response({"status": result}, status=status.HTTP_200_OK)
