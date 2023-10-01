"""Viewsets for the endpoints of 'Api' application v1."""

from django.contrib.auth import get_user_model
from rest_framework import mixins, viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated

from api.v1.serializers import (
    CategorySerializer,
    ProductSerializer,
    ShoppingCartSerializer,
    ShoppingCartDetailSerializer,
    SubCategorySerializer,
    UserSerializer,
)
from core.misc_constants import PAGE_CONSTANTS
from orders.models import ShoppingCart
from products.models import Category, Product, SubCategory

User = get_user_model()


class UserViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    """URL request handler for creating users."""

    name = "User resource"
    description = "API endpoints for creating users."

    queryset = User.objects.all()
    serializer_class = UserSerializer


class CategoryViewSet(
    mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet
):
    """URL requests handler to 'Categories' resource endpoints."""

    name = "Category resource"
    description = "API endpoints for viewing categories."

    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = PageNumberPagination
    pagination_class.page_size = PAGE_CONSTANTS["category_number_per_page"]


class SubCategoryViewSet(
    mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet
):
    """URL requests handler to 'SubCategories' resource endpoints."""

    name = "SubCategory resource"
    description = "API endpoints for viewing subcategories."

    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer
    pagination_class = PageNumberPagination
    pagination_class.page_size = PAGE_CONSTANTS["category_number_per_page"]


class ProductViewSet(
    mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet
):
    """URL requests handler to 'Products' resource endpoints."""

    name = "Product resource"
    description = "API endpoints for viewing products."

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = PageNumberPagination
    pagination_class.page_size = PAGE_CONSTANTS["product_number_per_page"]


class ShoppingCartViewset(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    """URL requests handler to 'ShoppingCarts' resource endpoints."""

    name = "ShoppingCart resource"
    description = "API endpoints for working with shopping carts."

    queryset = ShoppingCart.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = ShoppingCartSerializer

    def get_serializer_class(self):
        if self.action == "list":
            return ShoppingCartDetailSerializer
        else:
            return ShoppingCartSerializer

    def get_queryset(self):
        return ShoppingCart.objects.filter(customer=self.request.user)
