# Generated by Django 4.2.6 on 2023-11-29 21:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('carritos', '0003_notebook_ubicacion'),
    ]

    operations = [
        migrations.CreateModel(
            name='PC',
            fields=[
                ('serial', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('activo_fijo', models.CharField(max_length=20)),
                ('modelo', models.CharField(max_length=30)),
                ('carro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='carritos.carro')),
                ('marca', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='carritos.marca')),
                ('ubicacion', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='carritos.ubicacion')),
            ],
        ),
    ]
