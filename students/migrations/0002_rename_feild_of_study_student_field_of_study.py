# Generated by Django 5.0.6 on 2024-08-14 09:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='feild_of_study',
            new_name='field_of_study',
        ),
    ]