# Generated by Django 4.1.6 on 2023-02-28 12:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0002_tutorial_section_article'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='tutorial',
            new_name='teacher',
        ),
        migrations.AlterField(
            model_name='section',
            name='id_section',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='landing.section'),
        ),
    ]
