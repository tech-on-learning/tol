# Generated by Django 4.1.7 on 2023-07-09 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0005_alter_student_message_alter_student_q_certificate_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Date')),
                ('first_name', models.CharField(max_length=150, null=True, verbose_name='First name')),
                ('last_name', models.CharField(max_length=150, null=True, verbose_name='Last name')),
                ('email', models.EmailField(max_length=200, null=True, verbose_name='Your email')),
                ('set_education_level', models.CharField(choices=[('High School', 'High School'), ('University', 'University'), ('College', 'College'), ('MBA / Doctorat', 'MBA / Doctorat')], default='High School', max_length=150, verbose_name="What's your education level?")),
                ('course', models.CharField(help_text='e.g. Graphic design, Coding, Data analysis...', max_length=300, null=True, verbose_name='What topic you would like to teach?')),
                ('message', models.TextField(null=True, verbose_name='Tell us more about you, and how you can help with your skills')),
            ],
            options={
                'verbose_name': 'Teacher',
                'verbose_name_plural': 'Teachers',
            },
        ),
    ]
