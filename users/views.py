from django.contrib.auth import authenticate
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from swagger_parameters import *
from users.serializers import SignupSerializer, UserSerializer


# api/v1/users/signup/
class SignupAPIView(APIView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        operation_id="회원가입",
        operation_description="계정명, 이메일, 비밀번호를 입력받아 회원가입을 진행합니다.",
        request_body=USER_SIGNUP_REQUEST_BODY,
        responses={200: USER_SIGNUP_200_RESPONSE_BODY, 400: USER_SIGNUP_400_RESPONSE_BODY},
    )
    def post(self, request):
        serializer = SignupSerializer(data=request.data)

        if serializer.is_valid():
            user = serializer.save()

            data = {"username": user.username, "email": user.email, "message": "회원가입이 완료되었습니다."}

            return Response(data, status=status.HTTP_201_CREATED)

        return Response({"message": "회원가입을 실패하였습니다.", "error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


# api/v1/users/login/
class LoginView(APIView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        operation_id="로그인",
        operation_description="계정명, 비밀번호로 로그인합니다.",
        request_body=USER_LOGIN_REQUEST_BODY,
        responses={
            200: USER_LOGIN_200_RESPONSE_BODY,
            400: USER_LOGIN_400_RESPONSE_BODY,
            404: USER_LOGIN_404_RESPONSE_BODY,
        },
    )
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")

        if username is None or password is None:
            return Response({"message": "계정명,비밀번호는 필수 입력사항입니다."}, status=status.HTTP_400_BAD_REQUEST)

        # 해당하는 사용자가 있는지 판단
        user = authenticate(username=username, password=password)
        if user is None:
            return Response({"message": "사용자를 찾을 수 없습니다."}, status=status.HTTP_404_NOT_FOUND)

        UserSerializer(user)

        # 토큰 발급
        token = TokenObtainPairSerializer.get_token(user)
        refresh_token = str(token)
        access_token = str(token.access_token)

        res = Response(
            {"message": "로그인 성공하였습니다."},
            status=status.HTTP_200_OK,
        )

        res.set_cookie("access", access_token, httponly=True)
        res.set_cookie("refresh", refresh_token, httponly=True)

        return res
