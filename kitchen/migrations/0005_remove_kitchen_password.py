# Generated by Django 2.2.5 on 2019-09-12 16:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kitchen', '0004_auto_20190911_1354'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='kitchen',
            name='password',
        ),
    ]
