# Generated by Django 5.1.2 on 2024-10-31 15:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0021_personnel_university_position_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='personnel',
            old_name='university_position',
            new_name='department_position',
        ),
        migrations.RemoveField(
            model_name='personnel',
            name='position',
        ),
    ]