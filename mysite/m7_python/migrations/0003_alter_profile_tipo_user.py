# Generated by Django 4.0.3 on 2022-04-07 15:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('m7_python', '0002_rename_total_sqm_inmueble_terrain_sqm'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='tipo_user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='profile', to='m7_python.tipouser'),
        ),
    ]
