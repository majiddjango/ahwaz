from django.db import models

from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver



class MyUser(AbstractUser):
    is_store = models.BooleanField(default=False)
    is_seen = models.BooleanField(default=False)




class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    name = models.CharField('تام',max_length=50,blank=True, null=True)
    last_name = models.CharField('نام خانوادگی',max_length=50,blank=True, null=True)
    email = models.EmailField('ایمیل',max_length=50,blank=True, null=True)
    image = models.ImageField('تصویر کاربری',blank=True, null=True)
    phone = models.CharField('تلفن',max_length=15,blank=True, null=True)
    mobile = models.CharField('موبایل',max_length=15,blank=True,null=True)
    location = models.CharField('لوکیشن',max_length=100,blank=True, null=True)
    address = models.TextField('آدرس',blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name or self.user.username
    
    class Meta:
        ordering = ('-created_date',)
        verbose_name = 'پروفایل کاربری'
        verbose_name_plural = 'پروفایل ها'




@receiver(post_save,sender=MyUser)
def on_user_register(sender,instance,created,**kwargs):
    if created:
        prof = Profile.objects.create(
            user = instance,
            name = instance.first_name or None,
            last_name = instance.last_name or None,
            email = instance.email or None,
            
        )
    else:
        try:
            profile = instance.profile
        except Exception:
            prof = Profile.objects.create(
                user = instance,
                name = instance.first_name or None,
                last_name = instance.last_name or None,
                email = instance.email or None,
                
            )
        if instance.first_name:
            instance.profile.name = instance.first_name
        if instance.last_name:
            instance.profile.last_name = instance.last_name
        if instance.email:
            instance.profile.email = instance.email
        instance.profile.save()

            
