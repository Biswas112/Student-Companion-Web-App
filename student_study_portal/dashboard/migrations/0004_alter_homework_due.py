# Generated by Django 5.0.6 on 2024-06-23 04:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_homework_is_finished_alter_homework_due'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homework',
            name='due',
            field=models.DateTimeField(),
        ),
    ]
