# Generated by Django 5.0.6 on 2024-10-29 14:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0017_alter_personnel_employment_type_and_more'),
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
