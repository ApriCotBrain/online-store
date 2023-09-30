"""Viewsets for the endpoints of 'Api' application v1."""

from rest_framework import mixins, viewsets
from rest_framework.pagination import PageNumberPagination

from api.v1.serializers import (
    CategorySerializer,
    ProductSerializer,
    SubCategorySerializer,
)
from core.misc_constants import PAGE_CONSTANTS
from products.models import Category, Product, SubCategory


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
