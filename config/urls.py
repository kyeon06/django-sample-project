from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="Django Sample Project App",
        default_version="v1",
        description="Django를 활용하여 여러 기능들을 구현하는 샘플 프로젝트입니다.",
        contact=openapi.Contact(email="jkyeon06@gmail.com"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    # admin
    path("admin/", admin.site.urls),
    # api
    path("api/v1/users/", include("users.urls")),
    path("api/v1/users/", include("dj_rest_auth.urls")),
    path("api/v1/users/", include("allauth.urls")),
    # swagger
    path("swagger/", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
