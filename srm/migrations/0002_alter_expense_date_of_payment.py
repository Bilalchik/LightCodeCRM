# Generated by Django 4.1.6 on 2023-03-10 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('srm', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='date_of_payment',
            field=models.DateField(verbose_name='Дата'),
        ),
    ]
