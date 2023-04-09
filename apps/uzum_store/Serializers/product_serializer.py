from rest_framework import serializers
from rest_framework.fields import CurrentUserDefault
from rest_framework.serializers import ModelSerializer

from apps.uzum_store.Serializers import ImageModelSerializer, CategoryModelSerializer
from apps.uzum_store.models import Product


class ProductModelSerializer(ModelSerializer):
    user = serializers.HiddenField(default=CurrentUserDefault())

    class ProductModelSerializer(ModelSerializer):
        def to_representation(self, instance):
            represent = super().to_representation(instance)
            represent['images'] = ImageModelSerializer(instance.get_images.first()).data
            represent['category'] = CategoryModelSerializer(instance.category).data
            return represent

    class Meta:
        model = Product
        exclude = ('created_at', 'updated_at', 'slug')

