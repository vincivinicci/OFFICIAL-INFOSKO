# Generated by Django 5.1.3 on 2025-01-02 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0045_remove_roomschedule_class_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='roomschedule',
            name='schedule_type',
            field=models.CharField(choices=[('regular', 'Regular'), ('temporary', 'Temporary')], default='regular', max_length=10),
        ),
    ]
