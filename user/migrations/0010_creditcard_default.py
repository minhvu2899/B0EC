# Generated by Django 3.1.7 on 2021-06-13 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0009_creditcard'),
    ]

    operations = [
        migrations.AddField(
            model_name='creditcard',
            name='default',
            field=models.BooleanField(default=False),
        ),
    ]