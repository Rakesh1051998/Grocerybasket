# Generated by Django 2.2.2 on 2019-07-18 04:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grocery', '0002_auto_20190718_0931'),
    ]

    operations = [
        migrations.AlterField(
            model_name='details',
            name='price',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='details',
            name='quantity',
            field=models.IntegerField(),
        ),
    ]