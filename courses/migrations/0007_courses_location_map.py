# Generated by Django 4.1.7 on 2023-07-09 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0006_courses_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='courses',
            name='location_map',
            field=models.CharField(help_text='Insert the google map iFrame code', max_length=200, null=True, unique=True, verbose_name='Location map'),
        ),
    ]
