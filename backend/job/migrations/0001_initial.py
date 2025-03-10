# Generated by Django 5.1.4 on 2025-03-05 14:12

import django.contrib.gis.db.models.fields
import django.contrib.gis.geos.point
import django.core.validators
import django.db.models.deletion
import job.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Job",
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
                ("title", models.CharField(max_length=200, null=True)),
                ("description", models.TextField(null=True)),
                ("email", models.EmailField(max_length=254, null=True)),
                ("address", models.CharField(max_length=255, null=True)),
                (
                    "job_type",
                    models.CharField(
                        choices=[
                            ("Permanent", "Permanent"),
                            ("Temporary", "Temporary"),
                            ("Intership", "Intership"),
                        ],
                        default="Permanent",
                        max_length=10,
                    ),
                ),
                (
                    "education",
                    models.CharField(
                        choices=[
                            ("Bachelors", "Bachelors"),
                            ("Masters", "Masters"),
                            ("Phd", "Phd"),
                        ],
                        default="Bachelors",
                        max_length=10,
                    ),
                ),
                (
                    "industry",
                    models.CharField(
                        choices=[
                            ("Business", "Business"),
                            ("Information Technology", "It"),
                            ("Banking", "Banking"),
                            ("Education/Training", "Education"),
                            ("Telecommunication", "Telecommunication"),
                            ("Others", "Others"),
                        ],
                        default="Business",
                        max_length=30,
                    ),
                ),
                (
                    "experience",
                    models.CharField(
                        choices=[
                            ("No Experience", "No Experience"),
                            ("1 Years", "One Year"),
                            ("2 Years", "Two Year"),
                            ("3 Years above", "Three Year Plus"),
                        ],
                        default="No Experience",
                        max_length=20,
                    ),
                ),
                (
                    "salary",
                    models.IntegerField(
                        default=1,
                        validators=[
                            django.core.validators.MinValueValidator(1),
                            django.core.validators.MaxValueValidator(1000000),
                        ],
                    ),
                ),
                ("positions", models.IntegerField(default=1)),
                ("company", models.CharField(max_length=100, null=True)),
                (
                    "point",
                    django.contrib.gis.db.models.fields.PointField(
                        default=django.contrib.gis.geos.point.Point(0.0, 0.0), srid=4326
                    ),
                ),
                (
                    "last_date",
                    models.DateTimeField(default=job.models.return_date_time),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "user",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
