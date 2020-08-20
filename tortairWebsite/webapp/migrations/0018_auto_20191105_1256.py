# Generated by Django 2.2.5 on 2019-11-05 05:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0017_auto_20191102_1700'),
    ]

    operations = [
        migrations.CreateModel(
            name='Borro_order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Get_eqm_id', models.IntegerField(default=0)),
                ('Eqm_name', models.CharField(max_length=200, null=True)),
                ('Get_Amount', models.IntegerField(default=0)),
                ('date_br', models.DateField(default=datetime.date(2019, 11, 5), verbose_name='date published')),
                ('Date_repatriate', models.DateField(verbose_name='date published')),
            ],
        ),
        migrations.AlterField(
            model_name='borrow',
            name='date_br',
            field=models.DateField(default=datetime.date(2019, 11, 5), verbose_name='date published'),
        ),
    ]
