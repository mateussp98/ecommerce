# Generated by Django 3.2 on 2021-04-18 20:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0002_variação'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Variação',
            new_name='Variacao',
        ),
        migrations.AlterModelOptions(
            name='variacao',
            options={'verbose_name': 'Variação', 'verbose_name_plural': 'Variações'},
        ),
    ]
