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
from courses.models import Courses

# Rich Text Editor
from tinymce import models as tinymce_models

# Datetime
import datetime

#----------#
#  CHOICES #
#----------#
# Bool
yes = 'Yes'
no = 'No'
n = 'Maybe'
BOOL_CHOICES = [
    (yes, yes),
    (no, no),
    (n, n),
]

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


#----------------#
#  For students  #
#----------------#
class Student(models.Model):
    # Times
    h1 = 'Samedi - 9h - 17h'
    h2 = 'Dimanche - 9h - 17h'
    h3 = 'Samedi - 9h - 12h et Dimanche - 9h - 12h'
    SET_SCHEDULE_CHOICES = [
        (h1, h1),
        (h2, h2),
        (h3, h3),
    ]
    # Wishes
    h1 = 'En ligne'
    h2 = 'En presentiel'
    SET_WISHES_CHOICES = [
        (h1, h1),
        (h2, h2),
    ]
    # Hear US
    h1 = 'Site Web'
    h2 = 'Amis'
    h3 = 'Email'
    h4 = 'Whatsapp'
    h5 = 'Facebook'
    h6 = 'Twitter'
    h7 = 'Instagram'
    h8 = 'Television'
    SET_HEAR_US_CHOICES = [
        (h1, h1),
        (h2, h2),
        (h3, h3),
        (h4, h4),
        (h5, h5),
        (h6, h6),
        (h7, h7),
        (h8, h8),
    ]
    # Pricing
    h1 = '2,500 - 3,500 HTG'
    h2 = '3,500 - 5,500 HTG'
    h3 = '5,500 - 10,500 HTG'
    h4 = '10,500 HTG +'
    SET_PRICES_CHOICES = [
        (h1, h1),
        (h2, h2),
        (h3, h3),
        (h4, h4),
    ]

    date        =   models.DateTimeField(auto_now_add=True, null=True, verbose_name="Date")

    first_name  =   models.CharField(max_length=150, verbose_name='First name', null=True, blank=False)
    last_name   =   models.CharField(max_length=150, verbose_name='Last name', null=True, blank=False)
    email       =   models.EmailField(max_length=200, verbose_name='Your email', null=True, blank=False)

    course     =   models.ForeignKey(Courses, related_name='contact_student_course_rel', on_delete=models.SET_NULL, null=True, blank=False, verbose_name='What course you would like to learn?')

    set_schedule    =   models.CharField(max_length=150, choices=SET_SCHEDULE_CHOICES, default=h3, verbose_name="Quelle horaire vous serait confortable?")

    q_laptop        =   models.CharField(max_length=150, choices=BOOL_CHOICES, default=yes, verbose_name="Avez-vous un laptop?")
    q_wish          =   models.CharField(max_length=150, choices=SET_WISHES_CHOICES, default=h2, verbose_name="Comment souhaiteriez-vous participer a ce cours?")
    q_hearing_us    =   models.CharField(max_length=150, choices=SET_HEAR_US_CHOICES, default=h1, verbose_name="Comment avez-vous entendu parler de cet événement?")

    q_certificate    =   models.CharField(max_length=150, choices=BOOL_CHOICES, default=n, verbose_name="Souhaiteriez-vous obtenir un certificat?")
    q_price    =   models.CharField(max_length=150, choices=SET_PRICES_CHOICES, default=h2, verbose_name="Combien esperez vous la participation?")

    message     =   models.TextField(verbose_name='Tell us more about you, and how you want us to help you with this course', null=True, blank=False)

    class Meta:
        verbose_name = "Student"
        verbose_name_plural = "Students"

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.email}"


#---------------#
#  For Teacher  #
#---------------#
class Teacher(models.Model):

    # Education Level
    h1 = 'High School'
    h2 = 'University'
    h3 = 'College'
    h4 = 'MBA / Doctorat'
    SET_EDU_LEVEL_CHOICES = [
        (h1, h1),
        (h2, h2),
        (h3, h3),
        (h4, h4),
    ]

    date        =   models.DateTimeField(auto_now_add=True, null=True, verbose_name="Date")

    first_name  =   models.CharField(max_length=150, verbose_name='First name', null=True, blank=False)
    last_name   =   models.CharField(max_length=150, verbose_name='Last name', null=True, blank=False)
    email       =   models.EmailField(max_length=200, verbose_name='Your email', null=True, blank=False)

    set_education_level    =   models.CharField(max_length=150, choices=SET_EDU_LEVEL_CHOICES, default=h1, verbose_name="What's your education level?")

    course      =   models.CharField(max_length=300, verbose_name='What topic you would like to teach?', null=True, blank=False, help_text="e.g. Graphic design, Coding, Data analysis...")

    message     =   models.TextField(verbose_name='Tell us more about you, and how you can help with your skills', null=True, blank=False)

    class Meta:
        verbose_name = "Teacher"
        verbose_name_plural = "Teachers"

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.email}"
