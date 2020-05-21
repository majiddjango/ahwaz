from django.db import models

# Create your models here.
from core.models import Product,Store
from django.conf import settings
from django.shortcuts import reverse

class PostPay(models.Model):
    post = models.PositiveIntegerField('هزینه ارسال')
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'هزینه ارسال'
        verbose_name_plural = 'هزینه ارسال'
        ordering = ('-created_date',)

    def __str__(self):
        return f'{self.post}'

class Cart(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL,blank=True, null=True)
    closed = models.BooleanField(default=False)
    paid = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def total(self):
        items = self.items.all()
        sums = 0
        for item in items:
            sums += item.total_price()
        return sums

    def post_pay(self):
        if self.total() > 100000:
            return 0
        else:
            p = PostPay.objects.first()
            return p.post
    
    def total_with_pay(self):
        return self.total() + self.post_pay()
    

    class Meta:
        verbose_name = 'cart'
        verbose_name_plural = 'carts'
        ordering = ('-created_date',)

    def __str__(self):
        return f'{self.user} - {self.created_date}'
class Item(models.Model):
    cart = models.ForeignKey(Cart,on_delete=models.CASCADE ,verbose_name='cart',related_name='items')
    product = models.ForeignKey(Product,on_delete=models.SET_NULL,blank=True, null=True)
    quantity = models.BigIntegerField('quantity')
    price = models.PositiveIntegerField()
    name = models.CharField(max_length=200)
    store_name = models.CharField(max_length=200)
    sent = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'item'
        verbose_name_plural = 'items'
        ordering = ('cart',)

    def __str__(self):
        return f'{self.quantity} * {self.name}'
    
    def get_delete_url(self):
        return reverse('delete_item',kwargs={'id':self.id})
    def total_price(self):
        return self.quantity * self.price


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL,blank=True, null=True)
    cart = models.OneToOneField(Cart,on_delete=models.CASCADE ,verbose_name='cart',related_name='order')
    paid = models.BooleanField(default=False)
    first_name = models.CharField('نام',max_length=50)
    last_name = models.CharField('نام خانوادگی',max_length=50)
    telephone = models.CharField('تلفن',max_length=50)
    email = models.EmailField('ایمیل')
    address = models.TextField('آدرس')
    location = models.CharField('لوکیشن',max_length=50)
    total = models.BigIntegerField('جمع کل')
    is_seen = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    
    class Meta:
        verbose_name = 'سفارش'
        verbose_name_plural = 'سفارشات'
        ordering = ('-created_date',)

    def __str__(self):
        return f'{self.user} - {self.created_date}'
