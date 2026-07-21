from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.accounts.services.auth.register import RegisterService

from ..serializers import RegisterSerializer


class RegisterView(APIView):
    authentication_classes = ()
    permission_classes = ()

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        result = RegisterService.register(
            data=serializer.to_dto(),
        )

        return Response(result, status=status.HTTP_200_OK)
