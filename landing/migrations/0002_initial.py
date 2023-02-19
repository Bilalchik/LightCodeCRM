# Generated by Django 4.1.6 on 2023-02-19 14:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('landing', '0001_initial'),
        ('srm', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='courseforlanding',
            name='teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='srm.employee', verbose_name='Ментор'),
        ),
    ]
