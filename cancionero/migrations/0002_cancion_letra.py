# Generated by Django 4.2.1 on 2023-05-23 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cancionero', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cancion',
            name='letra',
            field=models.TextField(default='letra'),
            preserve_default=False,
        ),
    ]
