# Generated by Django 2.2.6 on 2019-10-30 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libro', '0003_auto_20191030_1252'),
    ]

    operations = [
        migrations.AddField(
            model_name='autor',
            name='fecha_creacion',
            field=models.DateField(auto_now=True, verbose_name='Fecha Creación'),
        ),
        migrations.AddField(
            model_name='libro',
            name='fecha_creacion',
            field=models.DateField(auto_now=True, verbose_name='Fecha Creación'),
        ),
    ]
