from django.urls import path, include
from rest_framework.routers import DefaultRouter

from posts.views import PhotoViewSet

router = DefaultRouter(trailing_slash=False)
router.register(r'photos', PhotoViewSet)

urlpatterns = [
    path('', include(router.urls)),

]

