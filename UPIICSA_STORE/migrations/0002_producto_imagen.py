# Generated by Django 5.0 on 2024-01-06 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UPIICSA_STORE', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='imagen',
            field=models.ImageField(default='default.png', upload_to='imagenes/'),
        ),
    ]
