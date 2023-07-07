# Generated by Django 4.1.7 on 2023-06-29 16:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import users.models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, null=True, unique=True)),
                ('bio', models.TextField(blank=True, help_text='300 character limit', null=True, verbose_name='Biography')),
                ('avatar', models.ImageField(blank=True, null=True, upload_to=users.models.Profile.path_and_rename, verbose_name='Profile Picture')),
                ('linkedin', models.URLField(blank=True, help_text='e.g. "https://www.linkedin.com/in/btm/"', null=True, verbose_name='LinkedIn')),
                ('instagram', models.URLField(blank=True, help_text='e.g. "https://instagram.com/bontimamitnews/"', null=True, verbose_name='Instagram')),
                ('twitter', models.URLField(blank=True, help_text='e.g. "https://twitter.com/bontimamitnews/"', null=True, verbose_name='Twitter')),
                ('facebook', models.URLField(blank=True, help_text='e.g. "https://facebook.com/bontimamitnews/"', null=True, verbose_name='Facebook')),
                ('website', models.URLField(blank=True, help_text='e.g. "https://btmht.com/"', null=True, verbose_name='Website')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name': 'Profile',
                'verbose_name_plural': 'Profiles',
                'db_table': 'users_profiles',
            },
        ),
    ]
