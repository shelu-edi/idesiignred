# Generated by Django 3.1.2 on 2021-09-23 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accessories', '0003_auto_20210919_0101'),
    ]

    operations = [
        migrations.AddField(
            model_name='accrecievedin',
            name='acc_id',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='accrecievedin',
            name='acc_name',
            field=models.CharField(default=1, max_length=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='accsentout',
            name='acc_id',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='accsentout',
            name='acc_name',
            field=models.CharField(default=1, max_length=1000),
            preserve_default=False,
        ),
    ]
