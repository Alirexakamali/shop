from rest_framework.response import Response
from rest_framework.views import APIView

from ..serializers import PasswordLoginSerializer
from apps.accounts.authentication.jwt import JWT


class PasswordLoginView(APIView):
    authentication_classes = ()
    permission_classes = ()

    def post(self, request):
        serializer = PasswordLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        tokens = JWT.create_tokens(
            serializer.validated_data["user"]
        )

        return Response(tokens)