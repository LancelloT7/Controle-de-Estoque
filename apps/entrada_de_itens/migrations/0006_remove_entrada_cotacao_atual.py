# Generated by Django 5.2.1 on 2025-05-28 18:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('entrada_de_itens', '0005_alter_entrada_nota_fiscal'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entrada',
            name='cotacao_atual',
        ),
    ]
