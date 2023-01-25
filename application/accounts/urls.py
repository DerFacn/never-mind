from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.index),
    path("accounts/signup/", views.signup),
    path("accounts/", include("django.contrib.auth.urls")),
    path("activate/<uidb64>/<token>", views.activate, name="activate"),
]