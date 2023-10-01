"""URLs configuration of the 'Api' application v1."""

from django.urls import include, path
from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter

from api.v1.views import (
    CategoryViewSet,
    ProductViewSet,
    ShoppingCartViewset,
    SubCategoryViewSet,
    UserViewSet,
)

router_v1 = DefaultRouter()

router_v1.register("categories", CategoryViewSet, basename="categories")
router_v1.register("subcategories", SubCategoryViewSet, basename="subcategories")
router_v1.register("products", ProductViewSet, basename="products")
router_v1.register("users", UserViewSet, basename="users")
router_v1.register("shopping_carts", ShoppingCartViewset, basename="shopping_carts")

urlpatterns = [
    path("", include(router_v1.urls)),
    path("api-token-auth/", views.obtain_auth_token),
]
