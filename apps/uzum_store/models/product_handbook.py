from django.db.models import Model, CharField, SlugField, ForeignKey, CASCADE, ImageField, IntegerField, TextField, \
    DateTimeField, TextChoices
from django.utils.text import slugify


class Category(Model):
    name = CharField(max_length=255)
    slug = SlugField(max_length=255, blank=True, null=True)

    def _get_unique_slug(self):
        slug = slugify(self.name)
        unique_slug = slug
        num = 1

        while Category.objects.filter(slug=unique_slug).exists():
            unique_slug = f'{slug}-{num}'
            num += 1
        return unique_slug

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.slug = self._get_unique_slug()
        if force_update is True:
            self.name = slugify(self.name)
        super().save(force_insert, force_update, using, update_fields)

    def __str__(self):
        return self.name


class SubCategory(Model):
    name = CharField(max_length=255)
    slug = SlugField(max_length=255, blank=True, null=True)
    parent = ForeignKey('Category', CASCADE, 'parents')

    def _get_unique_slug(self):
        slug = slugify(self.name)
        unique_slug = slug
        num = 1

        while Category.objects.filter(slug=unique_slug).exists():
            unique_slug = f'{slug}-{num}'
            num += 1
        return unique_slug

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.slug = self._get_unique_slug()
        if force_update is True:
            self.name = slugify(self.name)
        super().save(force_insert, force_update, using, update_fields)

    def __str__(self):
        return self.name


class Shop(Model):
    title = CharField(max_length=255)
    slug = SlugField(max_length=255, null=True, blank=True)
    image = ImageField(upload_to='shop/')
    description = TextField()
    merchant = ForeignKey('users.User', CASCADE, 'merchant', null=True, blank=True)
    created_at = DateTimeField(auto_now_add=True)

    def _get_unique_slug(self):
        slug = slugify(self.title)
        unique_slug = slug
        num = 1

        while Category.objects.filter(slug=unique_slug).exists():
            unique_slug = f'{slug}-{num}'
            num += 1
        return unique_slug

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.slug = self._get_unique_slug()
        if force_update is True:
            self.name = slugify(self.title)
        super().save(force_insert, force_update, using, update_fields)

    def __str__(self):
        return self.title


class Image(Model):
    image = ImageField(upload_to='images/')
    product = ForeignKey('Product', CASCADE)


class Cart(Model):
    class CartStatus(TextChoices):
        ACCEPTED = 'accepted', 'Accepted'
        PENDING = 'pending', 'Pending'
    user = ForeignKey('users.User', CASCADE, 'cart')
    product = ForeignKey('Product', CASCADE, 'product_cart')
    quantity = IntegerField(default=1)
    status = CharField(max_length=20, choices=CartStatus.choices, default=CartStatus.PENDING)

    def __str__(self):
        return f'{self.product}'


class Wishlist(Model):
    user = ForeignKey('users.User', CASCADE, 'wishlist')
    product = ForeignKey('Product', CASCADE, 'product_wishlist')

    def __str__(self):
        return f'{self.product}'


class Order(Model):
    user = ForeignKey('users.User', CASCADE)
    cart = ForeignKey('Cart', CASCADE)
    product = ForeignKey('Product', CASCADE)

    def __str__(self):
        return f"{self.product.name}"
