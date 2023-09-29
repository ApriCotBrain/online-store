"""Serializers for the endpoints of 'Api' application v1."""

from rest_framework import serializers

from products.models import Category, SubCategory


class CategorySerializer(serializers.ModelSerializer):
    """Serializer for categories."""

    class Meta:
        model = Category
        fields = (
            "id",
            "name",
            "slug",
            "image",
        )


class SubCategorySerializer(serializers.ModelSerializer):
    """Serializer for subcategories."""

    category = CategorySerializer()

    class Meta:
        model = SubCategory
        fields = (
            "id",
            "category",
            "name",
            "slug",
            "image",
        )
