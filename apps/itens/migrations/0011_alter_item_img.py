# Generated by Django 5.2.1 on 2025-05-27 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('itens', '0010_alter_item_options_alter_notafiscal_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='img',
            field=models.ImageField(blank=True, upload_to='itens/'),
        ),
    ]
