# Generated by Django 4.2.2 on 2023-09-26 18:24

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):
    dependencies = [
        ("finecap", "0006_alter_reserva_data"),
    ]

    operations = [
        migrations.AlterField(
            model_name="reserva",
            name="data",
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
