from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

urlpatterns = [
    # path('api-token-auth/', obtain_auth_token),
    path('api-jwt-auth/', TokenObtainPairView.as_view()),
    path('api-jwt-auth/refresh/', TokenRefreshView.as_view()),
    path('api-jwt-auth/verify/', TokenVerifyView.as_view()),
]

