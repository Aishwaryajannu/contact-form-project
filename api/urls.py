from django.urls import path
from .views import register
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

# Initialize urlpatterns properly before modifying it
urlpatterns = [
    path('register/', register, name='register'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
