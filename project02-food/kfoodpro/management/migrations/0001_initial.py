# Generated by Django 4.2.5 on 2023-09-25 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Manager",
            fields=[
                (
                    "id",
                    models.CharField(max_length=20, primary_key=True, serialize=False),
                ),
                ("pass1", models.CharField(max_length=20)),
                ("name", models.CharField(max_length=20)),
                ("errcount", models.IntegerField(default=0)),
            ],
        ),
    ]