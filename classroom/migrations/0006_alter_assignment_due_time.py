# Generated by Django 4.1.6 on 2023-03-29 10:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0005_assignment_assignment_name_ky_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignment',
            name='due_time',
            field=models.TimeField(default=datetime.time(16, 14, 26, 645027), verbose_name='Время сдачи'),
        ),
    ]
