# Generated by Django 3.1.7 on 2021-06-02 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0006_auto_20210529_1017'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderdetail',
            name='image',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='orderdetail',
            name='product_name',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
