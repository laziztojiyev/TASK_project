from django.db.models import F
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import GenericAPIView
from rest_framework.parsers import MultiPartParser
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, DjangoObjectPermissions
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from apps.uzum_store.Serializers import CartModelSerializer, WishlistModelSerializer, OrderModelSerializer, \
    ImageModelSerializer
from apps.uzum_store.Serializers.product_serializer import ProductModelSerializer
from apps.uzum_store.filters import ProductFilter
from apps.uzum_store.models import Category, SubCategory, Shop, Product
from apps.uzum_store.Serializers.product_handbook_serializers import CategoryModelSerializer, \
    SubCategoryModelSerializer, ShopModelSerializer
from apps.uzum_store.models.product_handbook import Cart, Wishlist, Order, Image
from users.permissions import IsOwner


# Create your views here.

class CategoryModelViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategoryModelSerializer
    lookup_field = 'slug'
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwner, DjangoObjectPermissions]
    parser_classes = (MultiPartParser, )

    def perform_create(self, serializer):
        # when a product is saved, its saved how it is the owner
        serializer.save(user=self.request.user)

    def get_queryset(self):
        # after get all products on DB it will be filtered by its owner and return the queryset
        owner_queryset = self.queryset.filter(user=self.request.user)
        return owner_queryset


class SubCategoryModelViewSet(ModelViewSet):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategoryModelSerializer
    lookup_field = 'slug'
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwner, DjangoObjectPermissions]
    parser_classes = (MultiPartParser,)

    def perform_create(self, serializer):
        # when a product is saved, its saved how it is the owner
        serializer.save(user=self.request.user)

    def get_queryset(self):
        # after get all products on DB it will be filtered by its owner and return the queryset
        owner_queryset = self.queryset.filter(user=self.request.user)
        return owner_queryset


class ShopModelViewSet(ModelViewSet):
    queryset = Shop.objects.all()
    serializer_class = ShopModelSerializer
    lookup_field = 'slug'
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwner, DjangoObjectPermissions]
    parser_classes = (MultiPartParser,)

    def perform_create(self, serializer):
        # when a product is saved, its saved how it is the owner
        serializer.save(user=self.request.user)

    def get_queryset(self):
        # after get all products on DB it will be filtered by its owner and return the queryset
        owner_queryset = self.queryset.filter(user=self.request.user)
        return owner_queryset

class CartModelViewSet(ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartModelSerializer
    lookup_url_kwarg = 'id'
    permission_classes = [IsAuthenticated, IsOwner, DjangoObjectPermissions]
    parser_classes = (MultiPartParser,)

    def perform_create(self, serializer):
        # when a product is saved, its saved how it is the owner
        serializer.save(user=self.request.user)

    def get_queryset(self):
        # after get all products on DB it will be filtered by its owner and return the queryset
        owner_queryset = self.queryset.filter(user=self.request.user)
        return owner_queryset

class WishlistModelViewSet(ModelViewSet):
    queryset = Wishlist.objects.all()
    serializer_class = WishlistModelSerializer
    lookup_url_kwarg = 'id'
    permission_classes = [IsAuthenticated, IsOwner, DjangoObjectPermissions]

    def perform_create(self, serializer):
        # when a product is saved, its saved how it is the owner
        serializer.save(user=self.request.user)

    def get_queryset(self):
        # after get all products on DB it will be filtered by its owner and return the queryset
        owner_queryset = self.queryset.filter(user=self.request.user)
        return owner_queryset


class OrderModelViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderModelSerializer
    lookup_url_kwarg = 'id'
    permission_classes = [IsAuthenticated, IsOwner, DjangoObjectPermissions]

    def get_queryset(self):
        qs = super().get_queryset()
        data = self.request.data
        cart = data.get('cart')
        product = data.get('product')
        quantity = Cart.objects.get(pk=cart).quantity
        Product.objects.filter(pk=product).update(amount=F('amount') - quantity)
        Cart.objects.filter(pk=cart).update(status='accepted')
        return qs


class ImageAPIView(GenericAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageModelSerializer
    parser_classes = (MultiPartParser,)

    def get(self, request):
        images = Image.objects.all()
        serializers = self.serializer_class(images, many=True)
        return Response(serializers.data)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


class ProductModelViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductModelSerializer
    lookup_field = 'slug'
    permission_classes = [IsAuthenticated, IsOwner, DjangoObjectPermissions]
    parser_classes = (MultiPartParser,)
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    filterset_class = ProductFilter
    search_fields = ['name']

    def perform_create(self, serializer):
        # when a product is saved, its saved how it is the owner
        serializer.save(user=self.request.user)

    def get_queryset(self):
        # after get all products on DB it will be filtered by its owner and return the queryset
        owner_queryset = self.queryset.filter(user=self.request.user)
        return owner_queryset
