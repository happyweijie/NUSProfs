from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

urlpatterns = [
    path('register', views.RegisterView.as_view(), name='register'),
    path("token",views.UserTokenObtainPairView.as_view(), name="token_obtain_pair"), # login
    path("token/refresh", TokenRefreshView.as_view(), name="token_refresh"), # refresh token
    path('logout', views.LogoutView.as_view(), name='logout'), # logout
    path('change_username', views.ChangeUsernameView.as_view(), name='change_username'), # change username
    path("change_password", views.ChangePasswordView.as_view(), name="change_password"), # change password
    path("whoami", views.profile, name="whoami"), # test protected test view
]