# Generated by Django 3.1.7 on 2021-06-13 16:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0007_product_option_product_option_value'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Product_Option',
            new_name='ProductOption',
        ),
        migrations.RenameModel(
            old_name='Product_Option_Value',
            new_name='ProductOptionValue',
        ),
    ]
