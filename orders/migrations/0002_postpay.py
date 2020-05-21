# Generated by Django 2.2.12 on 2020-05-04 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostPay',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post', models.PositiveIntegerField(verbose_name='هزینه ارسال')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'هزینه ارسال',
                'verbose_name_plural': 'هزینه ارسال',
                'ordering': ('-created_date',),
            },
        ),
    ]