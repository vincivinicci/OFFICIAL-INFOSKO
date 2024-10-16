# Generated by Django 5.0.6 on 2024-10-01 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_alter_personnel_employment_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personnel',
            name='employment_type',
            field=models.CharField(choices=[('select', 'Select'), ('full-time', 'Full-Time'), ('part-time', 'Part-Time'), ('key-person', 'Key Person')], default='select', max_length=10),
        ),
    ]