# Generated by Django 5.1.3 on 2024-11-23 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0013_alter_progresousuario_fecha_completado'),
    ]

    operations = [
        migrations.AddField(
            model_name='leccion',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='lecciones/'),
        ),
    ]
