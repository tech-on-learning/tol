# Generated by Django 4.1.7 on 2023-07-09 20:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0008_alter_courses_location_map'),
        ('contact', '0003_students'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Students',
            new_name='Student',
        ),
    ]