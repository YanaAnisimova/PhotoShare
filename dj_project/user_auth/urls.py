from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView


from user_auth.views import UserViewSet, LogoutView

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'users', UserViewSet)

urlpatterns = [
    path('rest-auth/', include('rest_framework.urls')),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/logout/', LogoutView.as_view(), name='token_logout'),
    path('', include(router.urls)),
]
