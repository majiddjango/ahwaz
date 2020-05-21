# Generated by Django 2.2.12 on 2020-05-21 07:39

import ckeditor.fields
import core.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20200502_1953'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['-created_date'], 'verbose_name': 'محصول', 'verbose_name_plural': 'محصولات'},
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='products', to='core.Category', verbose_name='دسته بندی'),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=ckeditor.fields.RichTextField(verbose_name='توضیحات'),
        ),
        migrations.AlterField(
            model_name='product',
            name='discounted_price',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='قیمت پس از کسر تخفیف'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to=core.models.product_image, verbose_name='تصویر محصول'),
        ),
        migrations.AlterField(
            model_name='product',
            name='is_active',
            field=models.BooleanField(default=False, verbose_name='آیا محصول فعال است'),
        ),
        migrations.AlterField(
            model_name='product',
            name='is_available',
            field=models.BooleanField(default=True, verbose_name='آیا محصول موجود است'),
        ),
        migrations.AlterField(
            model_name='product',
            name='is_deleted',
            field=models.BooleanField(default=False, verbose_name='محصول پاک شود'),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=200, verbose_name='نام محصول'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.PositiveIntegerField(verbose_name='قیمت محصول'),
        ),
        migrations.AlterField(
            model_name='product',
            name='store',
            field=models.ForeignKey(limit_choices_to={'is_active': True}, on_delete=django.db.models.deletion.CASCADE, related_name='products', to='core.Store', verbose_name='فروشگاه'),
        ),
    ]
