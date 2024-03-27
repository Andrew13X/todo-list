# Generated by Django 5.0.3 on 2024-03-24 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0003_alter_task_status"),
    ]

    operations = [
        migrations.AlterField(
            model_name="task",
            name="status",
            field=models.CharField(
                choices=[("Done", "Done"), ("Not done", "Not done")],
                default="Not done",
                max_length=8,
            ),
        ),
    ]
