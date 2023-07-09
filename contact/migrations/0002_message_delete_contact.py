# Generated by Django 4.1.7 on 2023-07-09 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Date')),
                ('first_name', models.CharField(max_length=150, null=True, verbose_name='First name')),
                ('last_name', models.CharField(max_length=150, null=True, verbose_name='Last name')),
                ('email', models.EmailField(max_length=200, null=True, verbose_name='Your email')),
                ('subject', models.CharField(max_length=250, null=True, verbose_name='Your subject')),
                ('message', models.TextField(null=True, verbose_name='Tell us about your concern')),
            ],
            options={
                'verbose_name': 'Message',
                'verbose_name_plural': 'Messages',
            },
        ),
        migrations.DeleteModel(
            name='Contact',
        ),
    ]