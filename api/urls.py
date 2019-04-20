from django.contrib import admin
from django.urls import path, include
from core.views import ClienteViewSet
from rest_framework import routers
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token

router = routers.DefaultRouter()
router.register(r'clientes', ClienteViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('login/', obtain_jwt_token),
    path('refresh-token/', refresh_jwt_token),
    path('api-token-verify/', verify_jwt_token),
]
