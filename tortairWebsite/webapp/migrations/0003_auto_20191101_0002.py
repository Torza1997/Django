# Generated by Django 2.2.5 on 2019-10-31 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_auto_20191031_2331'),
    ]

    operations = [
        migrations.AlterField(
            model_name='borrow',
            name='Get_username',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
