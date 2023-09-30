"""Models of 'products' app."""

from django.core.validators import RegexValidator
from django.db import models

from core.field_limits import FIELD_LIMITS
from core.field_regexes import FIELD_REGEXES

from products.validators import ImageWidthHeightValidator


class Category(models.Model):
    """Category model."""

    name = models.CharField(
        "name",
        unique=True,
        max_length=FIELD_LIMITS["category_name_max_char"],
        validators=(RegexValidator(FIELD_REGEXES["category_name"]),),
        help_text="Category's name",
    )
    slug = models.SlugField(
        "slug",
        max_length=FIELD_LIMITS["category_slug_max_char"],
        help_text="Category's slug",
    )
    image = models.ImageField(
        "image",
        help_text="Category's image",
        upload_to="media/category",
    )

    class Meta:
        verbose_name = "category"
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name


class SubCategory(models.Model):
    """SubCategory model."""

    category = models.ForeignKey(
        Category,
        verbose_name="category",
        help_text="Subcategory's category",
        on_delete=models.CASCADE,
        related_name="subcategories",
    )
    name = models.CharField(
        "name",
        unique=True,
        max_length=FIELD_LIMITS["subcategory_name_max_char"],
        validators=(RegexValidator(FIELD_REGEXES["subcategory_name"]),),
        help_text="Subcategory's name",
    )
    slug = models.SlugField(
        "slug",
        max_length=FIELD_LIMITS["subcategory_slug_max_char"],
        help_text="Subcategory's slug",
    )
    image = models.ImageField(
        "image",
        help_text="Subcategory's image",
        upload_to="media/subcategory",
    )

    class Meta:
        verbose_name = "subcategory"
        verbose_name_plural = "subcategories"
        constraints = (
            models.UniqueConstraint(
                fields=("name", "category"), name="unique_subcategory_category_together"
            ),
        )

    def __str__(self):
        return self.name


class Product(models.Model):
    """Product model."""

    subcategory = models.ForeignKey(
        SubCategory,
        verbose_name="subcategory",
        help_text="product's subcategory",
        on_delete=models.CASCADE,
        related_name="products",
    )
    name = models.CharField(
        "name",
        unique=True,
        max_length=FIELD_LIMITS["product_name_max_char"],
        validators=(RegexValidator(FIELD_REGEXES["product_name"]),),
        help_text="Subcategory's name",
    )
    slug = models.SlugField(
        "slug",
        max_length=FIELD_LIMITS["product_slug_max_char"],
        help_text="Product's slug",
    )
    image_small = models.ImageField(
        "small image",
        validators=(
            ImageWidthHeightValidator(
                max_width=FIELD_LIMITS["small_product_image_max_width"],
                max_height=FIELD_LIMITS["small_product_image_max_width"],
            ),
        ),
        help_text="Product's small image",
        upload_to="media/product/small",
    )
    image_medium = models.ImageField(
        "medium image",
        validators=(
            ImageWidthHeightValidator(
                max_width=FIELD_LIMITS["medium_product_image_max_width"],
                max_height=FIELD_LIMITS["medium_product_image_max_width"],
            ),
        ),
        help_text="Product's medium image",
        upload_to="media/product/medium",
    )
    image_large = models.ImageField(
        "large image",
        validators=(
            ImageWidthHeightValidator(
                max_width=FIELD_LIMITS["large_product_image_max_width"],
                max_height=FIELD_LIMITS["large_product_image_max_width"],
            ),
        ),
        help_text="Product's large image",
        upload_to="media/product/large",
    )
    price = models.DecimalField(
        "price",
        max_digits=FIELD_LIMITS["price_max_digits"],
        decimal_places=FIELD_LIMITS["price_decimal_places"],
        help_text="Product's price",
    )

    class Meta:
        verbose_name = "product"
        verbose_name_plural = "products"
        constraints = (
            models.UniqueConstraint(
                fields=("name", "subcategory"),
                name="unique_product_subcategory_together",
            ),
        )

    def __str__(self):
        return self.name
