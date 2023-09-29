"""URLs configuration of the 'Api' application v1."""

from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.v1.views import CategoryViewSet, SubCategoryViewSet

router_v1 = DefaultRouter()

router_v1.register("categories", CategoryViewSet, basename="categories")
router_v1.register("subcategories", SubCategoryViewSet, basename="subcategories")

urlpatterns = [path("", include(router_v1.urls))]