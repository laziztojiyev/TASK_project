from django_filters import FilterSet, NumberFilter

from apps.uzum_store.models import Product


class ProductFilter(FilterSet):
    from_price = NumberFilter(field_name='price', lookup_expr='gte')
    to_price = NumberFilter(field_name='price', lookup_expr='lte')

    class Meta:
        model = Product
        fields = ('from_price', 'to_price')