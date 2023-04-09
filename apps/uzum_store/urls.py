"""root URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.uzum_store.views import CategoryModelViewSet, SubCategoryModelViewSet, ShopModelViewSet, ImageAPIView, \
    CartModelViewSet, WishlistModelViewSet, OrderModelViewSet, ProductModelViewSet

routers = DefaultRouter()
routers.register('category', CategoryModelViewSet, basename='category')
routers.register('subcategory', SubCategoryModelViewSet, basename='subcategory')
routers.register('shop', ShopModelViewSet, basename='shop')
routers.register('cart', CartModelViewSet, basename='cart')
routers.register('wishlist', WishlistModelViewSet, basename='wishlist')
routers.register('order', OrderModelViewSet, basename='order')
routers.register('product', ProductModelViewSet, basename='product')

urlpatterns = [
    path('', include(routers.urls)),
    path('images/', ImageAPIView.as_view(), name='image')
]
