# Generated by Django 5.1.2 on 2024-10-31 21:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemon',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='pokemon_imagenes/'),
        ),
    ]
