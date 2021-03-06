# Generated by Django 2.2.5 on 2019-11-01 08:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0014_borrow_eqm_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='borrow',
            name='Status_borrow',
            field=models.BooleanField(default=0),
        ),
        migrations.AddField(
            model_name='borrow',
            name='Status_repatriate',
            field=models.BooleanField(default=0),
        ),
        migrations.AlterField(
            model_name='borrow',
            name='date_br',
            field=models.DateField(default=datetime.date(2019, 11, 1), verbose_name='date published'),
        ),
    ]
