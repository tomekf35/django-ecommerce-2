from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

app_name = "accounts"
urlpatterns = [
    path("login/", views.login_view, name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("signup/", views.SignupPageView.as_view(), name="signup"),
    path("<str:username>/", views.user_profile_view, name="user_profile"),
]
