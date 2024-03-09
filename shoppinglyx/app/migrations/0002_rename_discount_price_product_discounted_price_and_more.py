# Generated by Django 5.0.3 on 2024-03-08 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="product",
            old_name="discount_price",
            new_name="discounted_price",
        ),
        migrations.AlterField(
            model_name="product",
            name="category",
            field=models.CharField(
                choices=[
                    ("mobile", "Mobile"),
                    ("laptop", "Laptop"),
                    ("top_wear", "Top Wear"),
                    ("bottom_wear", "Bottom Wear"),
                ],
                max_length=100,
            ),
        ),
    ]