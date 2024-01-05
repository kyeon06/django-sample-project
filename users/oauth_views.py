import os

from django.shortcuts import redirect

# 구글 소셜로그인 변수 설정
state = os.environ.get("STATE")
BASE_URL = "http://127.0.0.1:8000/"
GOOGLE_CALLBACK_URI = BASE_URL + "api/v1/users/google/login/callback/"


# 구글 로그인
def google_login(request):
    scope = "https://www.googleapis.com/auth/userinfo.email"
    client_id = os.environ.get("SOCIAL_AUTH_GOOGLE_CLIENT_ID")
    return redirect(
        f"https://accounts.google.com/o/oauth2/v2/auth?client_id={client_id}&response_type=code&redirect_uri={GOOGLE_CALLBACK_URI}&scope={scope}"
    )
