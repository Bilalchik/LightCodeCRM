# Generated by Django 4.1.6 on 2023-02-28 19:48

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assignment_name', models.CharField(max_length=50, verbose_name='Название')),
                ('due_date', models.DateField(verbose_name='Срок сдачи')),
                ('due_time', models.TimeField(default=datetime.time(1, 48, 53, 127881), verbose_name='Время сдачи')),
                ('posted_date', models.DateField(auto_now_add=True, verbose_name='Дата создания')),
                ('instruction', models.TextField(verbose_name='Инструкция')),
                ('total_marks', models.PositiveSmallIntegerField(default=100, verbose_name='Максимальное количество баллов')),
            ],
            options={
                'verbose_name': 'Задание',
                'verbose_name_plural': 'Задания',
            },
        ),
        migrations.CreateModel(
            name='Classroom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('classroom_name', models.CharField(max_length=99, verbose_name='Название')),
                ('section', models.CharField(max_length=99, verbose_name='Раздел')),
                ('class_code', models.CharField(default='0000000', max_length=10)),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('classroom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classroom.classroom')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Студент')),
            ],
            options={
                'verbose_name': 'Студент',
                'verbose_name_plural': 'Студент',
            },
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('classroom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classroom.classroom')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Ментор')),
            ],
            options={
                'verbose_name': 'Ментор',
                'verbose_name_plural': 'Менторы',
            },
        ),
        migrations.CreateModel(
            name='Submission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('submitted_date', models.DateField(auto_now_add=True, verbose_name='Дата отправки')),
                ('submitted_time', models.TimeField(auto_now_add=True, verbose_name='Время отправки')),
                ('submitted_on_time', models.BooleanField(default=True, verbose_name='Отправлено вовремя?')),
                ('marks_alloted', models.PositiveSmallIntegerField(default=0, verbose_name='Оценка')),
                ('submission_file', models.FileField(upload_to='documents', verbose_name='Файл')),
                ('status', models.PositiveSmallIntegerField(choices=[(1, 'Отправлено'), (2, 'Переделать'), (3, 'Выполнено')], default=1)),
                ('assignment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classroom.assignment', verbose_name='Задание')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classroom.student', verbose_name='Студент')),
            ],
            options={
                'verbose_name': 'Задания студентов',
                'verbose_name_plural': 'Задания студентов',
            },
        ),
        migrations.AddField(
            model_name='assignment',
            name='classroom',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classroom.classroom'),
        ),
    ]
