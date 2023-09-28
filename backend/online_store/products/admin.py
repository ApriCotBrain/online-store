"""Admin site settings of the 'Products' application."""

from django.contrib import admin

from products.models import Category, SubCategory


class SubCategoryInline(admin.TabularInline):
    """Subcategories widget on the Category object creation page."""

    model = SubCategory


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """Representation of the Category model in the admin panel."""

    list_display = ("id", "name", "slug", "image")
    search_fields = ("name",)
    inlines = (SubCategoryInline,)


@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    """Representation of the SubCategory model in the admin panel."""

    list_display = ("id", "name", "slug", "image")
    search_fields = ("name",)
