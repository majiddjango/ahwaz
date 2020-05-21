# Generated by Django 3.0.5 on 2020-05-02 15:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_brand_slug'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='brand',
            options={'ordering': ['-created_date'], 'verbose_name': 'برند', 'verbose_name_plural': 'برند ها'},
        ),
        migrations.AlterField(
            model_name='product',
            name='brand',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='products', to='core.Brand'),
        ),
    ]
