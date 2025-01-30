from django.contrib import admin
from django.urls import path, include
from api.views import *
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/user/register/", CreateUserView.as_view(), name="register"),
    path("api/token/", TokenObtainPairView.as_view(), name="get_token"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="refresh"),
    path("api/", include("api.urls")),
    path("api/user/", UserView.as_view(), name="user"),
    path("api/user/update/", UpdateUserView.as_view(), name="user_update"),
    path("api/users/", UsersView.as_view(), name="users"),
]