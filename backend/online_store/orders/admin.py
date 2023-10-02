"""Admin site settings of the 'Orders' application."""

from django.contrib import admin

from orders.models import ShoppingCart


@admin.register(ShoppingCart)
class ShoppingCartAdmin(admin.ModelAdmin):
    """Representation of the ShoppingCart model in the admin panel."""

    list_display = (
        "id",
        "customer",
        "product",
        "amount",
    )
