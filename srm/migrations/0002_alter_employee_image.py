# Generated by Django 4.1.6 on 2023-02-19 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('srm', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='image',
            field=models.ImageField(default=1, upload_to='media/image', verbose_name='Фотография'),
            preserve_default=False,
        ),
    ]
