# Generated by Django 5.0.6 on 2024-06-25 13:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_alter_homework_due'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homework',
            name='due',
            field=models.DateTimeField(default=datetime.datetime(2024, 6, 25, 13, 33, 50, 512258, tzinfo=datetime.timezone.utc)),
        ),
    ]
