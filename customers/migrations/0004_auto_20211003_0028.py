# Generated by Django 3.1.2 on 2021-10-02 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0003_auto_20210918_1525'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='email_type',
            field=models.CharField(choices=[('Work', 'Work'), ('Personal', 'Personal')], default='Work', max_length=10),
        ),
        migrations.AlterField(
            model_name='customer',
            name='mobile_no_type',
            field=models.CharField(choices=[('Mobile', 'Mobile'), ('Home', 'Home'), ('Work', 'Work')], default='Mobile', max_length=10),
        ),
        migrations.AlterField(
            model_name='customer',
            name='salutation',
            field=models.CharField(choices=[('Mr', 'Mr'), ('Mrs', 'Mrs'), ('Miss', 'Miss')], default='Mr', max_length=10),
        ),
    ]
