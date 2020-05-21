from django.db import models

# Create your models here.

from django.conf import settings
from ckeditor.fields import RichTextField
from django.shortcuts import reverse
from django.contrib import messages

from django.db.models.signals import pre_save

class Title(models.Model):
    title = models.CharField('تایتل سایت',max_length=30)

    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'تایتل سایت'
        verbose_name_plural = 'تایتل سایت'

class Problem(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,blank=True, null=True)
    name = models.CharField('نام',max_length=50)
    last_name = models.CharField('نام خانوادگی',max_length=50)
    email = models.EmailField('ایمیل', max_length=254)
    problem = models.TextField('نظر یا شکایت')
    answer = RichTextField('جوابیه',blank=True, null=True)
    
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    is_seen = models.BooleanField(default=False)


    def __str__(self):
        return 'نظر : {}'.format(self.name)
    


    def save(self, *args, **kwargs):
        # @todo send email to user
        super(Problem, self).save(*args, **kwargs) 

    class Meta:
        verbose_name = 'نظر یا شکایت'
        verbose_name_plural = 'نظر ها و شکایات'


class About(models.Model):
    description = RichTextField()

    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=False)
    is_available = models.BooleanField(default=True)
    class Meta:
        verbose_name = 'در باره ما'
        verbose_name_plural = 'درباره ما'


