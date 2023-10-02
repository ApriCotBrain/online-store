"""Viewsets for the endpoints of 'Api' application v1."""

from django.contrib.auth import get_user_model
from django.db.models import Sum, F
from rest_framework import mixins, status, viewsets
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from api.v1.permissions import IsOwner
from api.v1.serializers import (
    CategorySerializer,
    ProductSerializer,
    ShoppingCartSerializer,
    ShoppingCartDetailSerializer,
    SubCategorySerializer,
    UserSerializer,
)
from api.v1.viewsets import GetPostPatchDeleteViewSet
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


class ShoppingCartViewset(GetPostPatchDeleteViewSet):
    """URL requests handler to 'ShoppingCarts' resource endpoints."""

    name = "ShoppingCart resource"
    description = "API endpoints for working with shopping carts."

    queryset = ShoppingCart.objects.all()
    permission_classes = (IsAuthenticated, IsOwner)
    serializer_class = ShoppingCartSerializer

    def get_serializer_class(self):
        if self.action == "list":
            return ShoppingCartDetailSerializer
        else:
            return ShoppingCartSerializer

    def get_queryset(self):
        return ShoppingCart.objects.filter(customer=self.request.user)

    @action(
        detail=False,
        methods=("GET",),
        url_path="total",
        permission_classes=(IsAuthenticated, IsOwner,),
    )
    def total(self, request):
        customer = request.user
        shopping_carts = ShoppingCart.objects.filter(customer=customer)
        total_products = shopping_carts.aggregate(total=Sum("amount"))["total"]
        total_price = shopping_carts.aggregate(
            total=Sum(F("product__price") * F("amount"))
        )["total"]

        serializer = ShoppingCartDetailSerializer(shopping_carts, many=True)
        product = serializer.data

        response_data = {
        "total_products": total_products,
        "total_price": total_price,
        "products": product,
        }

        return Response(response_data)
    
    @action(
        detail=False,
        methods=("DELETE",),
        url_path="clear",
        permission_classes=(IsAuthenticated, IsOwner,),
    )
    def clear(self, request):
        customer = request.user
        shopping_carts = ShoppingCart.objects.filter(customer=customer)
        shopping_carts.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
