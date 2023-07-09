from django.db import models
from django.urls import reverse

from imagekit.models import ProcessedImageField,ImageSpecField
from imagekit.processors import ResizeToFill

# UUID
import uuid

# Import Slugify
from django.utils.text import slugify

#-----------------------#
#  Message Form models  #
#-----------------------#
class Message(models.Model):

    date        =   models.DateTimeField(auto_now_add=True, null=True, verbose_name="Date")

    first_name  =   models.CharField(max_length=150, verbose_name='First name', null=True, blank=False)
    last_name   =   models.CharField(max_length=150, verbose_name='Last name', null=True, blank=False)
    email       =   models.EmailField(max_length=200, verbose_name='Your email', null=True, blank=False)
    subject     =   models.CharField(max_length=250, verbose_name='Your subject', null=True, blank=False)
    message     =   models.TextField(verbose_name='Tell us about your concern', null=True, blank=False)

    class Meta:
        verbose_name = "Message"
        verbose_name_plural = "Messages"

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.subject}"