# Generated by Django 5.0 on 2023-12-23 19:11

import uuid

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("menu", "0002_order_productinorderamount_order_products"),
    ]

    operations = [
        migrations.CreateModel(
            name="MenuSet",
            fields=[
                ("is_active", models.BooleanField(default=True)),
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("name", models.CharField(max_length=255)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.AddField(
            model_name="menu",
            name="menu_sets",
            field=models.ManyToManyField(
                blank=True, related_name="menus", to="menu.menuset"
            ),
        ),
        migrations.CreateModel(
            name="MenuSetStep",
            fields=[
                ("is_active", models.BooleanField(default=True)),
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("name", models.CharField(max_length=255)),
                ("ordering_number", models.PositiveIntegerField(default=0)),
                (
                    "menu_set",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="set_steps",
                        to="menu.menuset",
                    ),
                ),
                (
                    "products",
                    models.ManyToManyField(
                        blank=True, related_name="menu_set_steps", to="menu.product"
                    ),
                ),
            ],
            options={
                "unique_together": {("name", "menu_set")},
            },
        ),
    ]
