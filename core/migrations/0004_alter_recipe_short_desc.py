# Generated by Django 5.1.3 on 2024-11-20 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_recipe_short_desc_alter_recipe_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='short_desc',
            field=models.TextField(max_length=200),
        ),
    ]
