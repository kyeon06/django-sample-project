from django.urls import path
from rest_framework_simplejwt.views import (
    TokenBlacklistView,
    TokenObtainPairView,
    TokenRefreshView,
)

from users.oauth_views import google_login
from users.views import LoginView, SignupAPIView

urlpatterns = [
    path("signup/", SignupAPIView.as_view(), name="user-signup"),
    path("login/", LoginView.as_view(), name="user-login"),
    # path('logout/', LogoutView.as_view(), name='user-logout')
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("token/blacklist/", TokenBlacklistView.as_view(), name="token_blacklist"),
    # oauth
    path("google/login", google_login, name="google_login"),
    # path('google/login/callback/', google_callback, name='google_callback'),
    # path('google/login/finish/', GoogleLogin.as_view(), name='google_login_todjango'),
]
