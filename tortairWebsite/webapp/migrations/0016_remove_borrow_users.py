# Generated by Django 2.2.5 on 2019-11-01 15:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0015_auto_20191101_1545'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='borrow',
            name='users',
        ),
    ]
