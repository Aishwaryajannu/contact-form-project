from django.urls import path
from .views import ContactListCreateView, register
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path("register/", register, name="register"),  # ✅ User Registration
    path("login/", TokenObtainPairView.as_view(), name="token_obtain_pair"),  # ✅ JWT Login
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),  # ✅ JWT Refresh
    path("contacts/", ContactListCreateView.as_view(), name="contact-list"),  # ✅ Contacts API
]
