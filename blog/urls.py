from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('post', views.PostViewSet)  # 2개의 url 패턴 생성
# router.urls  # url pattern 리스트

urlpatterns = [
    path('public/', views.PublicPostListAPIView.as_view()),
    path('', include(router.urls)),
]
