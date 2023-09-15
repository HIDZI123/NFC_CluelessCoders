# Generated by Django 4.2 on 2023-09-15 20:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0002_disease_description"),
    ]

    operations = [
        migrations.AlterField(
            model_name="disease",
            name="drug",
            field=models.ForeignKey(
                blank=True, on_delete=django.db.models.deletion.CASCADE, to="main.drug"
            ),
        ),
    ]
