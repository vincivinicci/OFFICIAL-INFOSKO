# Generated by Django 5.1.3 on 2025-01-12 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0061_alter_semester_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='semester',
            name='name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
