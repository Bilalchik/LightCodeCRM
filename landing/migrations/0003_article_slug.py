# Generated by Django 4.1.6 on 2023-03-01 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0002_article_topic_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='slug',
            field=models.SlugField(default=1),
            preserve_default=False,
        ),
    ]