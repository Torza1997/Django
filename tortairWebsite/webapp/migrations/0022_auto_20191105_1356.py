# Generated by Django 2.2.5 on 2019-11-05 06:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0021_remove_borro_order_eqm_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='borro_order',
            old_name='Get_eqm_id',
            new_name='Eqm_name',
        ),
    ]
