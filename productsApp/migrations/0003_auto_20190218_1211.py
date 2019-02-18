# Generated by Django 2.1.5 on 2019-02-18 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productsApp', '0002_auto_20190216_1320'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='photo',
            field=models.ImageField(null=True, upload_to='products_images'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=15, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_code',
            field=models.IntegerField(null=True, unique=True),
        ),
    ]
