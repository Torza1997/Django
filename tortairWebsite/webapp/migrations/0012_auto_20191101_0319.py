# Generated by Django 2.2.5 on 2019-10-31 20:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0011_auto_20191101_0212'),
    ]

    operations = [
        migrations.RenameField(
            model_name='borrow',
            old_name='Get_username',
            new_name='First_name',
        ),
        migrations.RemoveField(
            model_name='borrow',
            name='Get_eqm_id',
        ),
    ]