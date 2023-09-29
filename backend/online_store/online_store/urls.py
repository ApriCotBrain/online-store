"""URL configuration of the 'online_store' application."""

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("api.urls")),
]
