# Generated by Django 4.1.6 on 2023-03-11 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0003_alter_section_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='section',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Описание для подраздела'),
        ),
    ]
