from django.contrib import admin
from django.contrib.admin import ModelAdmin

from apps.uzum_store.models import Category, SubCategory, Product, Shop, Wishlist, Cart, Order


# Register your models here.
@admin.register(Category)
class CategoryModelAdmin(ModelAdmin):
    pass


@admin.register(SubCategory)
class SubCategoryModelAdmin(ModelAdmin):
    pass


# class ProductModelAdmin(ModelAdmin):
#     def get_queryset(self, request):
#         qs = super(ProductModelAdmin, self).get_queryset(request)
#         return qs.filter(owner=request.user)
#

admin.site.register(Product)


@admin.register(Shop)
class ShopModelAdmin(ModelAdmin):
    pass


@admin.register(Wishlist)
class WishlistModelAdmin(ModelAdmin):
    pass


@admin.register(Cart)
class CartModelAdmin(ModelAdmin):
    pass


@admin.register(Order)
class OrderModelAdmin(ModelAdmin):
    pass



