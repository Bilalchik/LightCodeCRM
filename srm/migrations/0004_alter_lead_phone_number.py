# Generated by Django 4.1.6 on 2023-02-23 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('srm', '0003_lead_prepayment_student_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lead',
            name='phone_number',
            field=models.CharField(max_length=15, verbose_name='Номер телефона'),
        ),
    ]
