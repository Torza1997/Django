# Generated by Django 2.2.5 on 2019-10-31 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0013_borrow_last_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='borrow',
            name='Eqm_name',
            field=models.CharField(max_length=200, null=True),
        ),
    ]