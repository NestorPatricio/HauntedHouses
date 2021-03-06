# Generated by Django 4.0.3 on 2022-04-15 03:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('m7_python', '0006_alter_profile_is_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inmueble',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='profile',
            name='picture',
            field=models.URLField(blank=True),
        ),
    ]
