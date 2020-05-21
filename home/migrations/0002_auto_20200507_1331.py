# Generated by Django 2.2.12 on 2020-05-07 09:01

import ckeditor.fields
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='title',
            options={'verbose_name': 'تایتل سایت', 'verbose_name_plural': 'تایتل سایت'},
        ),
        migrations.AddField(
            model_name='problem',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='problem',
            name='is_seen',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='problem',
            name='modified_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='problem',
            name='answer',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='جوابیه'),
        ),
    ]