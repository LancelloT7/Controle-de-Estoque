# Generated by Django 5.2.1 on 2025-05-26 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('itens', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='quantidade',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
