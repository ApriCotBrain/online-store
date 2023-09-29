"""Admin site settings of the 'Products' application."""

from django.contrib import admin

from products.models import Category, SubCategory, Product


class SubCategoryInline(admin.TabularInline):
    """Subcategories widget on the Category object creation page."""

    model = SubCategory


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """Representation of the Category model in the admin panel."""

    list_display = ("id", "name", "slug", "image")
    search_fields = ("name",)
    inlines = (SubCategoryInline,)


class ProductInline(admin.TabularInline):
    """Products widget on the SubCategory object creation page."""

    model = Product


@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    """Representation of the SubCategory model in the admin panel."""

    list_display = ("id", "name", "slug", "image")
    search_fields = ("name",)
    inlines = (ProductInline,)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """Representation of the Product model in the admin panel."""

    list_display = (
        "id",
        "name",
        "slug",
        "price",
        "image_small",
        "image_medium",
        "image_large",
    )
    search_fields = ("name",)
