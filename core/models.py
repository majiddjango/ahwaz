from django.db import models

# Create your models here.

from mptt.models import MPTTModel, TreeForeignKey
from django.utils.text import slugify
from django_extensions.db.fields import AutoSlugField
from django.conf import settings
from ckeditor.fields import RichTextField
from PIL import Image
from django.shortcuts import reverse

# from django_comments.moderation import CommentModerator
# from django_comments_xtd.moderation import moderator
# from django_comments.signals import comment_was_posted

from django.contrib import messages

class Category(MPTTModel):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100,blank=True,null=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    def get_absolute_url(self):
        return reverse('category_detail', kwargs={"slug": self.slug})
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs): 
        self.slug = slugify(self.name,allow_unicode=True) 
        super(Category, self).save(*args, **kwargs) 

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
    class MPTTMeta:
        order_insertion_by = ['name']


# First, define the Manager subclass.
class AllManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_deleted=False)

class ActiveManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_deleted=False,is_active=True)

def store_image(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'stores/user_{0}/{1}'.format(instance.owner.id, filename)

def my_slugify_function(content):
    return slugify(content,allow_unicode=True)
class Store(models.Model):
    owner = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to=store_image)
    slug = AutoSlugField(populate_from='name',slugify_function=my_slugify_function)
    phone = models.CharField(max_length=15)
    mobile = models.CharField(max_length=15,blank=True,null=True)
    area = models.CharField(max_length=100)
    address = models.TextField(null=True)
    location = models.CharField(max_length=100,blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)

    objects = AllManager()
    actives = ActiveManager()
    def get_absolute_url(self):
        return reverse('store_detail', kwargs={"slug": self.slug})

    def __str__(self):
        return f'{self.name} ({self.id})'
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs) 
        img = Image.open(self.image.path)
        width, height = img.size  # Get dimensions

        if width > 300 and height > 300:
            # keep ratio but shrink down
            img.thumbnail((width, height))

        # check which one is smaller
        if height < width:
            # make square by cutting off equal amounts left and right
            left = (width - height) / 2
            right = (width + height) / 2
            top = 0
            bottom = height
            img = img.crop((left, top, right, bottom))

        elif width < height:
            # make square by cutting off bottom
            left = 0
            right = width
            top = 0
            bottom = width
            img = img.crop((left, top, right, bottom))

        if width > 300 and height > 300:
            img.thumbnail((300, 300))

        img.save(self.image.path)    # def save(self, *args, **kwargs):
    #     self.slug = slugify(self.name,allow_unicode=True)
    #     super(Product, self).save(*args, **kwargs) 


def product_image(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'stores/user_{0}/products/{1}'.format(instance.store.owner.id, filename)

class Brand(models.Model):
    name = models.CharField('اسم',max_length=30)
    slug = AutoSlugField(populate_from='name',slugify_function=my_slugify_function)
    image = models.ImageField('لوگو',blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ['-created_date'] 
        verbose_name = 'برند'
        verbose_name_plural = 'برند ها'
    
    def __str__(self):
        return self.name
    
class Product(models.Model):
    store = models.ForeignKey(Store,on_delete=models.CASCADE,related_name='products',limit_choices_to={'is_active':True},verbose_name='فروشگاه')
    category = models.ForeignKey(Category,on_delete=models.SET_NULL,related_name='products',blank=True, null=True,verbose_name='دسته بندی')
    name = models.CharField('نام محصول',max_length=200)
    slug = models.SlugField(max_length=200)
    brand = models.ForeignKey(Brand,blank=True, null=True,on_delete=models.SET_NULL,related_name='products')
    image = models.ImageField('تصویر محصول',upload_to=product_image)
    description = RichTextField('توضیحات')
    price = models.PositiveIntegerField('قیمت محصول')
    discounted_price = models.PositiveIntegerField('قیمت پس از کسر تخفیف',blank=True, null=True)

    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    is_seen = models.BooleanField(default=False)
    is_active = models.BooleanField('آیا محصول فعال است',default=False)
    is_available = models.BooleanField('آیا محصول موجود است',default=True)
    is_deleted = models.BooleanField('محصول پاک شود',default=False)
    
    objects = AllManager()
    actives = ActiveManager()

    class Meta:
        ordering = ['-created_date'] 
        verbose_name = 'محصول'
        verbose_name_plural = 'محصولات'
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('product', kwargs={"store": self.store.slug,'slug':self.slug})

    def get_delete_url(self):
        return reverse('store_delete_product',kwargs={'id':self.id})
    def get_update_url(self):
        return reverse('store_update_product',kwargs={'id':self.id})
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name,allow_unicode=True) 
        super(Product, self).save(*args, **kwargs) 
        img = Image.open(self.image.path)
        width, height = img.size  # Get dimensions

        if width > 300 and height > 300:
            # keep ratio but shrink down
            img.thumbnail((width, height))

        # check which one is smaller
        if height < width:
            # make square by cutting off equal amounts left and right
            left = (width - height) / 2
            right = (width + height) / 2
            top = 0
            bottom = height
            img = img.crop((left, top, right, bottom))

        elif width < height:
            # make square by cutting off bottom
            left = 0
            right = width
            top = 0
            bottom = width
            img = img.crop((left, top, right, bottom))

        if width > 300 and height > 300:
            img.thumbnail((300, 300))

        img.save(self.image.path)






# class ProductCommentModerator(CommentModerator):
#     email_notification = True
#     auto_moderate_field = 'created_date'
#     moderate_after = 0


# moderator.register(Product, ProductCommentModerator)
# moderator.register(Store, ProductCommentModerator)

# def messageMe(sender,comment,request,**kwagrs):
#     messages.success(request,'نظر شما ثبت شد. با تشکر')

# comment_was_posted.connect(messageMe)