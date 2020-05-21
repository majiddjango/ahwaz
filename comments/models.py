from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.utils.encoding import force_str


class AllManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_deleted=False)
    
    def for_model(self, model):
        """
        QuerySet for all comments for a particular model (either an instance or
        a class).
        """
        ct = ContentType.objects.get_for_model(model)
        qs = self.get_queryset().filter(content_type=ct,is_active=True,level=0)
        if isinstance(model, models.Model):
            qs = qs.filter(object_id=force_str(model._get_pk_val()))
        return qs
class ActiveManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_deleted=False,is_active=True)

# Create your models here.
class Comment(MPTTModel):
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,blank=True,null=True)
    name = models.CharField('نام و نام خانوادگی',max_length=100)
    email = models.EmailField('ایمیل', max_length=254,blank=True,null=True)
    comment = models.TextField('نظر',null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField('آیا نظر فعال است',default=False)
    is_deleted = models.BooleanField('آیا نظر پاک شود',default=False)
    is_seen = models.BooleanField(default=False)

    objects = AllManager()
    actives = ActiveManager()

    def __str__(self):
        if self.parent:
            return f'C:{self.parent.id}:{self.id}'
        else:
            return f'C:{self.id}'
    

    class Meta:
        verbose_name = 'نظر'
        verbose_name_plural = 'نظرات'
    class MPTTMeta:
        order_insertion_by = ['-created_date']


