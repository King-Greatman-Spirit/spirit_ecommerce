# Generated by Django 4.2.11 on 2024-06-06 03:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_item_quantity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='quantity',
        ),
        migrations.AddField(
            model_name='orderitem',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
    ]
