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
    product = models.ManyToManyField(
        Product,
        through='ProductAmount',
        verbose_name="product",
        help_text="Add to shopping cart",
        related_name="shopping_carts",
    )

    class Meta:
        verbose_name = "shopping cart"
        verbose_name_plural = "shopping carts"

    def __str__(self):
        return f'{self.customer}'
    

class ProductAmount(models.Model):
    """Binding model for the amount of products in the shopping cart."""

    shopping_cart = models.ForeignKey(
        ShoppingCart,
        verbose_name="shopping cart",
        on_delete=models.CASCADE,
        related_name='product_amounts',
    )
    product = models.ForeignKey(
        Product,
        verbose_name="product",
        help_text="product",
        on_delete=models.CASCADE,
        related_name='product_amounts',
    )
    amount = models.SmallIntegerField(
        verbose_name='amont',
        help_text="Specify the number of products.",
        validators=(MinValueValidator(AMOUNT_CONSTRANTS["product_amount_min_value"]),)
    )

    class Meta:
        verbose_name = 'product amount'
        verbose_name_plural = 'product amounts'

    def __str__(self):
        return f'{self.shopping_cart_id} {self.product_id}'
