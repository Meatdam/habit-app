from datetime import datetime

import pytz
from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated

from base.settings import TIME_ZONE
from users.models import User
from users.permissions import IsSuperuser
from users.serializers import UserSerializer


class UserListApiView(generics.ListAPIView):
    """
    API для получения списка пользователей
    """
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserCreateApiView(generics.CreateAPIView):
    """
    API для регистрации пользователя
    """
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        user = serializer.save(is_active=True)
        user.set_password(user.password)
        user.last_login = datetime.now(pytz.timezone(TIME_ZONE))
        user.save()


class UserRetrieveApiView(generics.RetrieveAPIView):
    """
    API для получения пользователя
    """
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserUpdateAPIView(generics.UpdateAPIView):
    """
    API для изменения пользователя
    """
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [AllowAny]

    def get_queryset(self):
        return User.objects.filter(id=self.request.user.id)


class UserDestroyAPIView(generics.DestroyAPIView):
    """
    API для удаления пользователя
    """
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated, IsSuperuser]
