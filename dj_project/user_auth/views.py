from rest_framework import viewsets, status
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from user_auth.models import User
from user_auth.permission import IsAdminOrModerator, IsSimpleUserOwner
from user_auth.serializer import UserSerializer, RefreshTokenSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        permission_classes = []
        if self.action == 'create':
            permission_classes = [AllowAny]
        elif self.action == 'list':
            permission_classes = [IsAdminOrModerator]
        elif self.action == 'retrieve':
            permission_classes = [IsAuthenticated]
        elif self.action == 'update' or self.action == 'partial_update' or self.action == 'destroy':
            permission_classes = [IsSimpleUserOwner]
        return [permission() for permission in permission_classes]


class LogoutView(GenericAPIView):
    serializer_class = RefreshTokenSerializer

    def post(self, request, *args):
        sz = self.get_serializer(data=request.data)
        sz.is_valid(raise_exception=True)
        sz.save()
        return Response({'detail': 'Successfully logged out.'}, status=status.HTTP_204_NO_CONTENT)
