# Generated by Django 3.1.2 on 2021-09-16 13:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cutting', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recievedin',
            old_name='order_received',
            new_name='order_recieved',
        ),
    ]
