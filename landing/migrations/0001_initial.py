# Generated by Django 4.1.6 on 2023-02-19 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LearningFormat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Формат обучения',
                'verbose_name_plural': 'Форматы обучения',
            },
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70)),
                ('direction', models.CharField(max_length=50)),
                ('description', models.TextField(verbose_name='Описание')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
            ],
            options={
                'verbose_name': 'Отзыв',
                'verbose_name_plural': 'Отзывы',
            },
        ),
        migrations.CreateModel(
            name='StudyingTime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Время обучения',
                'verbose_name_plural': 'Время обучения',
            },
        ),
        migrations.CreateModel(
            name='CourseForLanding',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=123, verbose_name='Название')),
                ('slug', models.SlugField()),
                ('cover', models.ImageField(upload_to='media/image/', verbose_name='Обложка')),
                ('description', models.TextField(verbose_name='Описание о языке')),
                ('additional_info', models.TextField(blank=True, null=True, verbose_name='Информация о курсе')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('is_active', models.BooleanField(default=True, verbose_name='Активен')),
                ('format', models.ManyToManyField(to='landing.learningformat', verbose_name='Формат обучения')),
                ('studying_time', models.ManyToManyField(to='landing.studyingtime', verbose_name='Время обучения')),
            ],
            options={
                'verbose_name': 'Курс для Лэндинга',
                'verbose_name_plural': 'Курс для Лэндинга',
            },
        ),
    ]