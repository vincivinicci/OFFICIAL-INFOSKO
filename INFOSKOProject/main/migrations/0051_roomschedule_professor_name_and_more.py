# Generated by Django 5.1.3 on 2025-01-03 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0050_alter_room_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='roomschedule',
            name='professor_name',
            field=models.CharField(default='Unknown Professor', max_length=100),
        ),
        migrations.AddField(
            model_name='roomschedule',
            name='section_name',
            field=models.CharField(default='Unknown Section', max_length=100),
        ),
        migrations.AddField(
            model_name='roomschedule',
            name='subject_name',
            field=models.CharField(default='Unknown Subject', max_length=100),
        ),
    ]
