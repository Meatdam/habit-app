from django.urls import path

from users.apps import UsersConfig

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from users.views import UserListApiView, UserCreateApiView, UserRetrieveApiView, UserDestroyAPIView, \
    UserUpdateAPIView

app_name = UsersConfig.name

urlpatterns = [
    path('users/', UserListApiView.as_view(), name='users'),
    path('create/', UserCreateApiView.as_view(), name='create_users'),
    path('detail/<int:pk>/', UserRetrieveApiView.as_view(), name='detail_users'),
    path('delete/<int:pk>/', UserDestroyAPIView.as_view(), name='delete_users'),
    path('update/<int:pk>/', UserUpdateAPIView.as_view(), name='update_users'),
    # token
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
