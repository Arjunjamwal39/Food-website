# Generated by Django 3.2.2 on 2021-05-19 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_product_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Logo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo', models.ImageField(upload_to='static/images/logo/')),
            ],
        ),
        migrations.AlterField(
            model_name='product',
            name='discription',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
    ]
