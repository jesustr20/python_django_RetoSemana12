# Generated by Django 2.2.6 on 2019-11-03 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libro', '0006_editorial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=255, verbose_name='Titulo')),
                ('apellido', models.CharField(max_length=255, verbose_name='Titulo')),
                ('fecha_registro', models.DateField(verbose_name='Fecha Registro')),
            ],
            options={
                'verbose_name': 'Cliente',
                'verbose_name_plural': 'Clientes',
                'ordering': ['nombre'],
            },
        ),
    ]
