# Generated by Django 3.2.2 on 2021-05-20 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_auto_20210520_1035'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='conf_password',
            field=models.CharField(default='', max_length=60),
        ),
    ]
