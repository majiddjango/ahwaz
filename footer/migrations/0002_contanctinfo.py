# Generated by Django 2.2.12 on 2020-05-07 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('footer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContanctInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('t', models.CharField(choices=[('e', 'Email'), ('t', 'Telephone')], max_length=2)),
                ('value', models.CharField(max_length=20)),
            ],
        ),
    ]
