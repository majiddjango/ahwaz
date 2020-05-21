from django.db import models

# Create your models here.

from django.conf import settings
from ckeditor.fields import RichTextField
from django.shortcuts import reverse
from django.contrib import messages



class Footer(models.Model):
    description = RichTextField('توضیحات فوتر')

    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name = 'فوتر'
        verbose_name_plural = 'فوتر'




LINK_CHOICES = ( 
    ("yt", "Youtube"), 
    ("tw", "Twitter"), 
    ("gp", "GooglePlus"), 
    ("tl", "Telegram"), 
    ("fb", "Facebook"), 
    ('li','LinkedIn'),
    ('in','Instagram')
) 
  
# declaring a Student Model 
  
class SocialNetworksLink(models.Model):
    footer = models.ForeignKey(Footer,on_delete=models.SET_NULL,related_name='socials',blank=True, null=True)
    name = models.CharField('نام',max_length=2,choices = LINK_CHOICES, )
    url = models.URLField('آدرس')


class ContanctInfo(models.Model):
    footer = models.ForeignKey(Footer,on_delete=models.SET_NULL,related_name='contacts',blank=True, null=True)
    name = models.CharField(max_length=20)
    t = models.CharField(max_length=2,choices=(
        ('e','Email'),
        ('t','Telephone')
    ))
    value = models.CharField(max_length=20)