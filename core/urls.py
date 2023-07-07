from django.urls import path
from . import views


app_name = "core"
urlpatterns = [
    path("", views.index_page_view, name="index"),
    path("shop/", views.shop_page_view, name="shop"),
    path("about/", views.about_page_view, name="about"),
    path("contact/", views.contact_page_view, name="contact"),
    path("vendor/", views.vendor_page_view, name="vendor"),
]
