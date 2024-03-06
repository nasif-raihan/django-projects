# Generated by Django 5.0.3 on 2024-03-06 19:05

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Product",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=100)),
                ("selling_price", models.FloatField()),
                ("discount_price", models.FloatField()),
                ("description", models.TextField()),
                ("brand", models.CharField(max_length=100)),
                (
                    "category",
                    models.CharField(
                        choices=[
                            ("Mobile", "Mobile"),
                            ("Laptop", "Laptop"),
                            ("Top Wear", "Top Wear"),
                            ("Bottom Wear", "Bottom Wear"),
                        ],
                        max_length=100,
                    ),
                ),
                ("product_image", models.ImageField(upload_to="product_images")),
            ],
        ),
        migrations.CreateModel(
            name="Customer",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("city", models.CharField(max_length=100)),
                ("locality", models.CharField(max_length=100)),
                ("zipcode", models.IntegerField(max_length=100)),
                (
                    "division",
                    models.CharField(
                        choices=[
                            ("dhaka", "Dhaka"),
                            ("khulna", "Khulna"),
                            ("sylhet", "Sylhet"),
                            ("rangpur", "Rangpur"),
                            ("barishal", "Barishal"),
                            ("rajshahi", "Rajshahi"),
                            ("mymensingh", "Mymensingh"),
                            ("chattogram", "Chattogram"),
                        ],
                        max_length=100,
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="OrderPlaced",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("quantity", models.PositiveIntegerField(default=1)),
                ("ordered_date", models.DateTimeField(auto_now_add=True)),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("packed", "Packed"),
                            ("accepted", "Accepted"),
                            ("canceled", "Canceled"),
                            ("delivered", "Delivered"),
                            ("on_the_way", "On the way"),
                        ],
                        max_length=100,
                    ),
                ),
                (
                    "customer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="app.customer"
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="app.product"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Cart",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("quantity", models.PositiveIntegerField(default=1)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="app.product"
                    ),
                ),
            ],
        ),
    ]