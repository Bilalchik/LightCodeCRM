# Generated by Django 4.1.6 on 2023-04-06 18:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0003_alter_assignment_due_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignment',
            name='due_time',
            field=models.TimeField(default=datetime.time(0, 59, 53, 609767), verbose_name='Время сдачи'),
        ),
    ]