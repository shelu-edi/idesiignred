# Generated by Django 3.1.2 on 2021-10-04 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ladiesstock',
            name='balance_quantity',
            field=models.IntegerField(max_length=9999),
        ),
        migrations.AlterField(
            model_name='ladiesstock',
            name='quantity',
            field=models.IntegerField(max_length=9999),
        ),
    ]
