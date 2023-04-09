from django.db.models import Model, CharField, DecimalField, JSONField, IntegerField, SlugField, DateTimeField, \
    ForeignKey, CASCADE, TextField
from django.utils.text import slugify


class Product(Model):
    name = CharField(max_length=255)
    price = DecimalField(decimal_places=2, max_digits=9)
    description = TextField()
    characteristic = JSONField(default=dict)
    quantity = IntegerField(default=1)
    on_sale = IntegerField(default=0)
    slug = SlugField(max_length=255, null=True, blank=True)
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)
    shipping_cost = IntegerField(default=0)
    category = ForeignKey('SubCategory', CASCADE, 'category')
    shop = ForeignKey('Shop', CASCADE, 'shop')
    user = ForeignKey('users.User', CASCADE, 'user_product')
    amount = IntegerField(default=1)

    def _get_unique_slug(self):
        slug = slugify(self.name)
        unique_slug = slug
        num = 1

        while Product.objects.filter(slug=unique_slug).exists():
            unique_slug = f'{slug}-{num}'
            num += 1
        return unique_slug

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.slug = self._get_unique_slug()
        if force_update is True:
            self.name = slugify(self.name)
        super().save(force_insert, force_update, using, update_fields)

    @property
    def get_images(self):
        return self.image_set.all()

    def __str__(self):
        return self.name

    def decrease_stock(self, quantity):
        if self.amount >= quantity:
            self.amount -= quantity
            self.save()
        else:
            raise ValueError("Not enough stock")

    def increase_stock(self, quantity):
        self.amount += quantity
        self.save()
