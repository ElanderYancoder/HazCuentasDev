# Generated by Django 5.1.3 on 2024-11-25 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0015_retroalimentacion_moderada'),
    ]

    operations = [
        migrations.AddField(
            model_name='insigniausuario',
            name='motivo',
            field=models.TextField(blank=True, null=True),
        ),
    ]
