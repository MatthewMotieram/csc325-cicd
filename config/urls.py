from django.contrib import admin
from django.shortcuts import redirect
from django.urls import include, path

urlpatterns = [
    path("", lambda request: redirect("hello")),
    path("admin/", admin.site.urls),
    path("api/", include("api.urls")),
]
