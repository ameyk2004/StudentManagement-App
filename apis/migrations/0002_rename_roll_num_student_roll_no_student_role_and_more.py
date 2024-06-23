# Generated by Django 5.0.6 on 2024-06-23 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='roll_num',
            new_name='roll_no',
        ),
        migrations.AddField(
            model_name='student',
            name='role',
            field=models.CharField(default=0, max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='student',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]