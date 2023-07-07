from django.urls import reverse
from django.db import models

# Image Processing
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

# UUID
import uuid

# Import Slugify
from django.utils.text import slugify

# Signals
from django.db.models.signals import post_save
from django.dispatch import receiver

# Django Models
from django.contrib.auth.models import User

#----------------------#
#  USER PROFILE MODEL  #
#----------------------#
class Profile(models.Model):

    # Path to media
    def path_and_rename(instance, filename):
        master_path = "avatar/users"
        ext = filename.split('.')[-1]
        # get filename
        path = f"{master_path}/{instance.user.username}/"
        path_file_name = f"{instance.user.username}-techonlearning-{uuid.uuid4()}"
        filename = '{}/{}.{}'.format(path, path_file_name, ext)
        # return the whole path to the file
        return filename

    # Account
    user                =   models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=False, verbose_name='User')

    # UUID
    uuid                =   models.UUIDField(primary_key=False, unique=True, blank=False, null=True, default=uuid.uuid4, editable=False)

    # Settings / Personal Info
    title               =   models.CharField(max_length=500, null=True, blank=False, verbose_name='Title', help_text="e.g. Data Analyst, Graphic Designer, Photographer...")
    bio                 =   models.TextField(null=True, blank=True, verbose_name="Biography", help_text="300 character limit")

    # Images
    avatar              =   models.ImageField(upload_to=path_and_rename, null=True, blank=True, verbose_name='Profile Picture')
    avatar_thumb_small  =   ImageSpecField(source='avatar',
                                    processors=[ResizeToFill(100, 100)],
                                    format='JPEG')
    avatar_thumb_profil =   ImageSpecField(source='avatar',
                                    processors=[ResizeToFill(500, 500)],
                                    format='JPEG',
                                    options={'quality': 80})
    avatar_thumb_25     =   ImageSpecField(source='avatar',
                                    processors=[ResizeToFill(25, 25)],
                                    format='JPEG',
                                    options={'quality': 100})
    avatar_thumb_70     =   ImageSpecField(source='avatar',
                                    processors=[ResizeToFill(70, 70)],
                                    format='JPEG',
                                    options={'quality': 90})
    avatar_thumb_150    =   ImageSpecField(source='avatar',
                                    processors=[ResizeToFill(150, 150)],
                                    format='JPEG',
                                    options={'quality': 80})

    # Settings / Social Links
    linkedin            =   models.URLField(null=True, blank=True, verbose_name="LinkedIn", help_text="e.g. \"https://www.linkedin.com/in/teachonlearning/\"")
    instagram           =   models.URLField(null=True, blank=True, verbose_name="Instagram", help_text="e.g. \"https://instagram.com/teachonlearning/\"")
    twitter             =   models.URLField(null=True, blank=True, verbose_name="Twitter", help_text="e.g. \"https://twitter.com/teachonlearning/\"")
    facebook            =   models.URLField(null=True, blank=True, verbose_name="Facebook", help_text="e.g. \"https://facebook.com/teachonlearning/\"")

    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"
        db_table = "users_profiles"

    def __str__(self):
        if self.user.get_full_name():
            return f"{self.user.get_full_name()}"
        return f"@{self.user.username}"

    def get_absolute_url(self):
        return reverse("user", args=[str(self.user.username)])

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()