from django.urls import path
from rest_framework_simplejwt.views import (
    TokenBlacklistView,
    TokenObtainPairView,
    TokenRefreshView,
)

from users.views import LoginView, SignupAPIView

urlpatterns = [
    path("signup/", SignupAPIView.as_view(), name="user-signup"),
    path("login/", LoginView.as_view(), name="user-login"),
    # path('logout/', LogoutView.as_view(), name='user-logout')
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("token/blacklist/", TokenBlacklistView.as_view(), name="token_blacklist"),
]
