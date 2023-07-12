from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

app_name = "accounts"
urlpatterns = [
    path("login/", views.login_view, name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("signup/", views.SignupPageView.as_view(), name="signup"),
    path("<str:username>/", views.user_profile_view, name="user_profile"),
    path(
        "<str:username>/edit_personal/",
        views.user_edit_personal_view,
        name="user_edit_personal",
    ),
    path(
        "<str:username>/edit_address/",
        views.user_edit_address_view,
        name="user_edit_address",
    ),
    path(
        "<str:username>/edit_address/form/<int:address_id>",
        views.user_edit_address_form_view,
        name="user_edit_address_form",
    ),
    path(
        "<str:username>/edit_phone/",
        views.user_edit_phone_view,
        name="user_edit_phone",
    ),
]
