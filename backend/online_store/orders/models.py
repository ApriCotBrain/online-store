"""Models of 'orders' app."""

from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator
from django.db import models

from core.misc_constants import AMOUNT_CONSTRANTS
from products.models import Product

User = get_user_model()


class ShoppingCart(models.Model):
    """ShoppingCart model."""

    customer = models.ForeignKey(
        User,
        verbose_name="customer",
        help_text="Shoping cart owner",
        on_delete=models.CASCADE,
        related_name="shopping_carts",
    )
    products = models.ForeignKey(
        Product,
        verbose_name="product",
        help_text="Product",
        on_delete=models.CASCADE,
        related_name="shopping_carts",
    )
    amounts = models.SmallIntegerField(
        verbose_name="amont",
        help_text="Product's amount",
        validators=(MinValueValidator(AMOUNT_CONSTRANTS["product_amount_min_value"]),),
    )

    class Meta:
        verbose_name = "shopping cart"
        verbose_name_plural = "shopping carts"
        constraints = (
            models.UniqueConstraint(
                fields=("customer", "products"),
                name="unique_customer_products_together",
            ),
        )

    def __str__(self):
        return f"{self.products.name}{self.amounts}"
