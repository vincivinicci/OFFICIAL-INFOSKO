# Generated by Django 5.0.6 on 2024-10-29 14:52

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0018_rename_university_position_personnel_department_position_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='personnel',
            old_name='department_position',
            new_name='university_position',
        ),
        migrations.AddField(
            model_name='personnel',
            name='position',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
    ]
