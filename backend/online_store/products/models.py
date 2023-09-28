"""Models of 'products' app."""

from django.core.validators import RegexValidator
from django.db import models

from core.field_limits import FIELD_LIMITS
from core.field_regexes import FIELD_REGEXES


class Category(models.Model):
    """Category model."""

    name = models.CharField(
        "name",
        unique=True,
        max_length=FIELD_LIMITS["category_name_max_char"],
        validators=(
            RegexValidator(
                FIELD_REGEXES["category_name"]
            ),
        ),
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
        validators=(
            RegexValidator(
                FIELD_REGEXES["subcategory_name"]
            ),
        ),
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
