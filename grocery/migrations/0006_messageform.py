# Generated by Django 2.2.2 on 2019-08-01 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grocery', '0005_detail_units'),
    ]

    operations = [
        migrations.CreateModel(
            name='MessageForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=200)),
                ('Email_id', models.CharField(max_length=200)),
                ('Contact_no', models.IntegerField()),
                ('Message', models.TextField()),
                ('Date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]