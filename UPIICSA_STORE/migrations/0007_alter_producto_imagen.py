# Generated by Django 5.0 on 2024-01-07 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UPIICSA_STORE', '0006_usuario_whatsapp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='imagen',
            field=models.ImageField(default='default.png', upload_to=''),
        ),
    ]
