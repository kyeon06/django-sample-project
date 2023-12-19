from drf_yasg import openapi

# 회원가입 관련
USER_SIGNUP_REQUEST_BODY = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'username': openapi.Schema(type=openapi.TYPE_STRING, description='계정명'),
        'email': openapi.Schema(type=openapi.TYPE_STRING, description='이메일'),
        'password': openapi.Schema(type=openapi.TYPE_STRING, description='비밀번호'),
    },
    required=['username', 'email' ,'password']
)

USER_SIGNUP_200_RESPONSE_BODY = openapi.Schema(
    '200',
    type=openapi.TYPE_OBJECT,
    properties={
        'username': openapi.Schema(type=openapi.TYPE_STRING, description='계정명'),
        'email': openapi.Schema(type=openapi.TYPE_STRING, description='이메일'),
        'message': openapi.Schema(type=openapi.TYPE_STRING, description='회원가입이 완료되었습니다.'),
    }
)

USER_SIGNUP_400_RESPONSE_BODY = openapi.Schema(
    '400',
    type=openapi.TYPE_OBJECT,
    properties={
        'message': openapi.Schema(type=openapi.TYPE_STRING, description='회원가입을 실패하였습니다.'),
        'error': openapi.Schema(type=openapi.TYPE_STRING, description='error'),
    }
)

# 로그인 관련
USER_LOGIN_REQUEST_BODY = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'username': openapi.Schema(type=openapi.TYPE_STRING, description='계정명'),
        'password': openapi.Schema(type=openapi.TYPE_STRING, description='비밀번호')
    },
    required=['username', 'password']
)

USER_LOGIN_200_RESPONSE_BODY = openapi.Schema(
    '200',
    type=openapi.TYPE_OBJECT,
    properties={
        'message': openapi.Schema(type=openapi.TYPE_STRING, description='로그인 성공하였습니다.'),
    }
)

USER_LOGIN_404_RESPONSE_BODY = openapi.Schema(
    '404',
    type=openapi.TYPE_OBJECT,
    properties={
        'message': openapi.Schema(type=openapi.TYPE_STRING, description='사용자를 찾을 수 없습니다.'),
    }
)

USER_LOGIN_400_RESPONSE_BODY = openapi.Schema(
    '400',
    type=openapi.TYPE_OBJECT,
    properties={
        'message': openapi.Schema(type=openapi.TYPE_STRING, description='계정명,비밀번호는 필수 입력사항입니다.'),
    }
)