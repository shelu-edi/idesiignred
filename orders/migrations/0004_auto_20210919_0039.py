# Generated by Django 3.1.2 on 2021-09-18 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_auto_20210919_0022'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderreceiving',
            name='order_no',
            field=models.CharField(max_length=1000, unique=True),
        ),
    ]