# Generated by Django 5.1.7 on 2025-03-08 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Category",
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
                ("name", models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name="Cuisine",
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
                ("name", models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name="Recipe",
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
                ("title", models.CharField(max_length=30)),
                ("description", models.TextField(default="")),
                (
                    "ingredients",
                    models.TextField(
                        default="", help_text="Separate ingredients with commas."
                    ),
                ),
                (
                    "prep_time",
                    models.PositiveIntegerField(
                        help_text="Preparation time in minutes."
                    ),
                ),
                (
                    "cook_time",
                    models.PositiveIntegerField(help_text="Cooking time in minutes."),
                ),
                ("servings", models.PositiveIntegerField()),
                ("method", models.TextField(default="")),
                ("image", models.ImageField(upload_to="images/")),
                ("category", models.ManyToManyField(to="recipes.category")),
                ("cuisine", models.ManyToManyField(to="recipes.cuisine")),
            ],
        ),
    ]
