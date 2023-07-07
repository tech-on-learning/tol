from django.urls import reverse
from django.db import models

# Import Hitcount
from hitcount.models import HitCountMixin, HitCount
from django.contrib.contenttypes.fields import GenericRelation

# UUID
import uuid

# Signals
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver

# Image Processing
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

# Other Models
from users.models import Profile

# Datetime
import datetime


#---------#
# Courses #
#---------#
class Contact(models.Model):
    pass