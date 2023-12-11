from django.urls import path

from users.views import LoginView, SignupAPIView

urlpatterns = [
    path('signup/', SignupAPIView.as_view(), name='user-signup'),
    path('login/', LoginView.as_view(), name='user_login'),
    # path('logout/', LogoutView.as_view(), name='user_logout')
]