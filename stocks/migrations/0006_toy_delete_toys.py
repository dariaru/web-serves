# Generated by Django 4.1.1 on 2022-09-27 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0005_remove_users_date_modified'),
    ]

    operations = [
        migrations.CreateModel(
            name='Toy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('price', models.CharField(max_length=30)),
                ('dicription', models.CharField(max_length=255)),
            ],
        ),
        migrations.DeleteModel(
            name='Toys',
        ),
    ]