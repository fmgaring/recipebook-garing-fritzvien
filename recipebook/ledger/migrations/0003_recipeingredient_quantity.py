# Generated by Django 4.2.9 on 2024-03-04 01:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ledger', '0002_rename_quantity_recipeingredient_ingredient'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipeingredient',
            name='quantity',
            field=models.CharField(default='something', max_length=100),
        ),
    ]