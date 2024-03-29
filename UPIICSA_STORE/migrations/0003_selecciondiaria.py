# Generated by Django 5.0 on 2024-01-06 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UPIICSA_STORE', '0002_producto_imagen'),
    ]

    operations = [
        migrations.CreateModel(
            name='SeleccionDiaria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_seleccion', models.DateField(unique=True)),
                ('productos', models.ManyToManyField(related_name='seleccion_diaria', to='UPIICSA_STORE.producto')),
            ],
        ),
    ]
