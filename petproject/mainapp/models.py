from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

User = get_user_model()

# Create your models here.

class Cathegory(models.Model):

    name = models.CharField(max_length=255, verbose_name='Cathegory name')
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name


class Product(models.Model):

    class Meta:
        abstract = True

    cathegory = models.ForeignKey(Cathegory, verbose_name='Cathegory', on_delete=models.CASCADE)
    title = models.CharField(max_length=255, verbose_name='Naming')
    slug = models.SlugField(unique=True)
    image = models.ImageField(verbose_name='Image')
    description = models.TextField(verbose_name='description', null=True)
    price = models.DecimalField(max_digits=9, decimal_places=9, verbose_name='Price')


    def __str__(self):
        return self.title





class CartProduct(models.Model):

    user = models.ForeignKey('customer', verbose_name='Customer', on_delete=models.CASCADE)
    cart = models.ForeignKey('cart', verbose_name='Cart', on_delete=models.CASCADE, related_name='Related_product')
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    quantity = models.PositiveIntegerField(default=1)
    final_price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Total')


    def __str__(self):
        return 'Product: {} (For cart)'.format(self.product.title)


class Cart(models.Model):

    owner = models.ForeignKey('Customer', verbose_name='Owner', on_delete=models.CASCADE)
    products = models.ManyToManyField(CartProduct, blank=True, related_name='Related_cart')
    total_products = models.PositiveIntegerField(default=0)


class Customer(models.Model):

    user = models.ForeignKey(User, verbose_name='User', on_delete=models.CASCADE)
    phone = models.CharField(max_length=20, verbose_name='Phone')
    adress = models.CharField(max_length=255, verbose_name='Adress')

    def __str__():
        return 'Customer: {} {}'.format(self.user.first_name, self.user.last_name)



class Laptop(Product):

    diagonal = models.CharField(max_length=255, verbose_name='Diagonal')
    display_type = models.CharField(max_length=255, verbose_name='Display_type')
    proc_freq = models.CharField(max_length=255, verbose_name='Processor_frequency')
    ram = models.CharField(max_length=255, verbose_name='Ram')
    video = models.CharField(max_length=255, verbose_name='Graphics')
    time_without_charge = models.CharField(max_length=255, verbose_name='Battery_resource')

    def __str__():
        return '{} : {}'.format(self.cathegory.name, self.title)


class Smartphone(Product):
    diagonal = models.CharField(max_length=255, verbose_name='Diagonal')
    display_type = models.CharField(max_length=255, verbose_name='Display_type')
    resolution = models.CharField(max_length=255, verbose_name='Resolution')
    acc_volume = models.CharField(max_length=255, verbose_name='Battery_volume')
    ram = models.CharField(max_length=255, verbose_name='Ram')
    sd = models.BooleanField(default=True, verbose_name='Sd_card_support')
    sd_volume_max = models.CharField(max_length=255, verbose_name='Max_volume_sd_card')
    main_cam_mp = models.CharField(max_length=255, verbose_name='Main_cam')
    front_cam_mp = models.CharField(max_length=255, verbose_name='Front_cam')

    def __str__():
        return '{} : {}'.format(self.cathegory.name, self.title)
