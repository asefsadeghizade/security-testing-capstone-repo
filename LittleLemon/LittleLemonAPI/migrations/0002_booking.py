# Generated by Django 5.0.7 on 2024-08-01 01:05

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("LittleLemonAPI", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Booking",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                ("no_of_guests", models.IntegerField()),
                ("bookingDate", models.DateTimeField()),
            ],
        ),
    ]
