# Generated by Django 3.1.7 on 2021-06-03 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0013_auto_20210603_2148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.IntegerField(choices=[('1', 'Chờ xác nhận'), ('2', 'Đang xử lí'), ('3', 'Đang giao hàng'), ('4', 'Đã hoàn thành'), ('5', 'Đã hủy')], default=('1', 'Chờ xác nhận'), max_length=2),
        ),
    ]
