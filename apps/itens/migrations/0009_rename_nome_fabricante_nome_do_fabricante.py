# Generated by Django 5.2.1 on 2025-05-27 15:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('itens', '0008_remove_item_nota_fiscal'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fabricante',
            old_name='nome',
            new_name='nome_do_fabricante',
        ),
    ]
