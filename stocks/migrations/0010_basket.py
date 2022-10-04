# Generated by Django 4.1.1 on 2022-09-28 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0009_alter_users_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='Basket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField(max_length=11)),
                ('toy_id', models.IntegerField(max_length=11)),
                ('number_of_toys', models.IntegerField(max_length=20)),
            ],
            options={
                'db_table': 'basket',
                'managed': False,
            },
        ),
    ]
