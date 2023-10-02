"""Serializers for the endpoints of 'Api' application v1."""

from django.contrib.auth import get_user_model
from rest_framework import serializers

from orders.models import ShoppingCart
from products.models import Category, Product, SubCategory

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    """Serializer for user creation."""

    class Meta:
        model = User
        fields = ("username", "password")

    def create(self, validated_data):
        password = validated_data.pop("password")
        user = User.objects.create(**validated_data)
        user.set_password(password)
        user.save()

        return user


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


class ProductSerializer(serializers.ModelSerializer):
    """Selializer for products."""

    category = serializers.SerializerMethodField()
    subcategory = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = (
            "id",
            "name",
            "slug",
            "category",
            "subcategory",
            "image_small",
            "image_medium",
            "image_large",
            "price",
        )

    def get_category(self, obj):
        return obj.subcategory.category.name

    def get_subcategory(self, obj):
        return obj.subcategory.name


class ShoppingCartDetailSerializer(serializers.ModelSerializer):
    """Selializer for viewing shopping carts."""

    product = ProductSerializer(read_only=True)
    total = serializers.SerializerMethodField()

    class Meta:
        model = ShoppingCart
        fields = ("product", "amount", "total")

    def get_total(self, obj):
        return obj.product.price * obj.amount


class ShoppingCartSerializer(serializers.Serializer):
    """Selializer for create, update shopping carts."""

    customer = serializers.HiddenField(default=serializers.CurrentUserDefault())
    amount = serializers.IntegerField()
    product = serializers.PrimaryKeyRelatedField(
        required=True, queryset=Product.objects.all()
    )

    def create(self, validated_data):
        customer = self.context["request"].user
        amount = validated_data["amount"]
        product = validated_data["product"]

        existed = ShoppingCart.objects.filter(customer=customer, product=product)

        if existed:
            existed = existed[0]
            existed.amount += amount
            existed.save()
        else:
            existed = ShoppingCart.objects.create(**validated_data)

        return existed

    def update(self, instance, validated_data):
        instance.amount = validated_data["amount"]
        instance.save()
        return instance
