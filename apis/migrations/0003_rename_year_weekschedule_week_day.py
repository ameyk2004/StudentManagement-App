# Generated by Django 5.0.6 on 2024-06-25 05:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0002_remove_weekschedule_dayschedule_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='weekschedule',
            old_name='year',
            new_name='week_day',
        ),
    ]