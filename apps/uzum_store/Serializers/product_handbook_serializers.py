from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework.fields import CurrentUserDefault
from rest_framework.serializers import ModelSerializer

from apps.uzum_store.models import Category, SubCategory, Shop
from apps.uzum_store.models.product_handbook import Image, Cart, Order, Wishlist


class CategoryModelSerializer(ModelSerializer):
    def validate(self, attrs):
        if Category.objects.filter(name=attrs['name']).exists():
            raise ValidationError('this name exact')
        return attrs

    class Meta:
        model = Category
        fields = ('name', )


class SubCategoryModelSerializer(ModelSerializer):
    def validate(self, attrs):
        if SubCategory.objects.filter(name=attrs['name']).exists():
            raise ValidationError('this name exact')
        return attrs

    class Meta:
        model = SubCategory
        fields = ('name', 'parent')


class ShopModelSerializer(ModelSerializer):
    def validate(self, attrs):
        if Shop.objects.filter(title=attrs['title']).exists():
            raise ValidationError('this name exact')
        return attrs

    class Meta:
        model = Shop
        fields = ('title', )


class ImageModelSerializer(ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'


class CartModelSerializer(ModelSerializer):
    user = serializers.HiddenField(default=CurrentUserDefault())

    class Meta:
        model = Cart
        fields = '__all__'


class OrderModelSerializer(ModelSerializer):
    user = serializers.HiddenField(default=CurrentUserDefault())

    class Meta:
        model = Order
        fields = '__all__'


class WishlistModelSerializer(ModelSerializer):
    user = serializers.HiddenField(default=CurrentUserDefault())

    class Meta:
        model = Wishlist
        fields = '__all__'
