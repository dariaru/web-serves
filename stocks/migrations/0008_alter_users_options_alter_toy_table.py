# Generated by Django 4.1.1 on 2022-09-28 09:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0007_alter_toy_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='users',
            options={'managed': False},
        ),
        migrations.AlterModelTable(
            name='toy',
            table='toys',
        ),
    ]
