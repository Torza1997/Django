# Generated by Django 2.2.5 on 2019-11-15 23:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0022_auto_20191105_1356'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('head', models.CharField(max_length=200)),
                ('body', models.TextField(max_length=500)),
            ],
        ),
        migrations.AlterField(
            model_name='borro_order',
            name='date_br',
            field=models.DateField(default=datetime.date(2019, 11, 16), verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='borrow',
            name='date_br',
            field=models.DateField(default=datetime.date(2019, 11, 16), verbose_name='date published'),
        ),
    ]