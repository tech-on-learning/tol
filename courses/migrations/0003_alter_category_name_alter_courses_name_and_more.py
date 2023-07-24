# Generated by Django 4.1.7 on 2023-07-24 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_alter_courses_location_alter_courses_location_map'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=200, null=True, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='courses',
            name='name',
            field=models.CharField(max_length=300, null=True, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='guide',
            name='name',
            field=models.TextField(blank=True, help_text='What people will learn in this course', null=True, verbose_name='Guide'),
        ),
        migrations.AlterField(
            model_name='tags',
            name='name',
            field=models.CharField(max_length=200, null=True, verbose_name='Name'),
        ),
    ]
