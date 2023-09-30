"""Models of 'orders' app."""

from django.contrib.auth import get_user_model
from django.db import models

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
    product = models.ManyToManyField(
        Product,
        verbose_name="product",
        help_text="Add to shopping cart",
        related_name="shopping_carts",
    )

    class Meta:
        verbose_name = "shopping cart"
        verbose_name_plural = "shopping carts"

    def __str__(self):
        return f'{self.customer}'
