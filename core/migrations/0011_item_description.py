# Generated by Django 4.2.11 on 2024-06-06 03:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_item_discount_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='description',
            field=models.TextField(default='Item Description'),
            preserve_default=False,
        ),
    ]
