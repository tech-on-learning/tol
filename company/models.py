from django.db import models
from django.urls import reverse

from imagekit.models import ProcessedImageField,ImageSpecField
from imagekit.processors import ResizeToFill

# UUID
import uuid

# Import Slugify
from django.utils.text import slugify

#-----------------------#
#  Testimonials models  #
#-----------------------#

class Testimonials(models.Model):

    # Path to media
    def path_to_avatar(instance, filename):
        master_path = "testimonials/avatar"
        ext = filename.split('.')[-1]
        # get filename
        path = f"{master_path}/{slugify(instance.name)}/"
        path_file_name = f"{uuid.uuid4()}"
        filename = '{}/{}.{}'.format(path, path_file_name, ext)
        # return the whole path to the file
        return filename

    name            =   models.CharField(max_length=200, null=True, blank=False, verbose_name='Name', unique=True)
    message         =   models.TextField(null=True, blank=False, verbose_name="Message")

    title           =   models.CharField(max_length=200, null=True, blank=False, verbose_name='Title', unique=False)

    # Avatar Picture
    avatar                  =   models.ImageField(upload_to=path_to_avatar, null=True, blank=True, verbose_name='Profil Picture')
    avatar_thumb            =   ImageSpecField(source='avatar',
                                    format='JPEG',
                                    options={'quality': 30})
    avatar_thumb_small      =   ImageSpecField(source='avatar',
                                    processors=[ResizeToFill(100, 100)],
                                    format='JPEG')

    created_at      =   models.DateTimeField(auto_now_add=True, null=True, blank=False)
    last_edit       =   models.DateTimeField(auto_now=True, null=True, blank=False, verbose_name="Updated On")

    class Meta:
        verbose_name = 'Testimonial'
        verbose_name_plural = 'Testimonials'

    def __str__(self):
        return self.name