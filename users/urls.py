from django.urls import path

from users.views import SignupAPIView

urlpatterns = [
    path('signup/', SignupAPIView.as_view(), name='user-signup'),
]