# Generated by Django 4.2 on 2023-05-07 02:36

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("task_log", "0004_remove_task_goals"),
    ]

    operations = [
        migrations.RenameField(
            model_name="artifact",
            old_name="reference",
            new_name="storage",
        )
    ]