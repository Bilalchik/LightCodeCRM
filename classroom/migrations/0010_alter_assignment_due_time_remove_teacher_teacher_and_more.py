# Generated by Django 4.1.6 on 2023-02-27 04:37

import datetime
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('classroom', '0009_submission_status_alter_assignment_due_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignment',
            name='due_time',
            field=models.TimeField(default=datetime.time(10, 37, 23, 286409), verbose_name='Время сдачи'),
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='teacher',
        ),
        migrations.AddField(
            model_name='teacher',
            name='teacher',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, verbose_name='Ментор'),
        ),
    ]