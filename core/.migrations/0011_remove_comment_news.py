# Generated by Django 2.2.6 on 2019-11-08 17:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_auto_20191108_1925'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='news',
        ),
    ]