# Generated by Django 5.0 on 2024-01-25 10:44

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0004_lawyerprofile"),
    ]

    operations = [
        migrations.CreateModel(
            name="VerifyToken",
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
                ("token", models.CharField(max_length=255)),
            ],
        ),
    ]