# Generated by Django 5.0.4 on 2024-07-05 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_remove_item_description_remove_item_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='birthday',
            field=models.CharField(max_length=150, null=True),
        ),
    ]