# Generated by Django 4.2.1 on 2023-05-29 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cancionero', '0002_cancion_letra'),
    ]

    operations = [
        migrations.AddField(
            model_name='cancion',
            name='nro_bp',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cancion',
            name='nro_sp',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
