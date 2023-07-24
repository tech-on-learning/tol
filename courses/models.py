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

# Rich Text Editor
from tinymce import models as tinymce_models

# Datetime
import datetime

#--------#
# STATUS #
#--------#
published = 'Published'
draft = 'Draft'
STATUS = [
    (published, published),
    (draft, draft),
]

#----------#
# Category #
#----------#
class Category(models.Model):

    # Info
    name            =   models.CharField(max_length=200, null=True, blank=False, verbose_name='Name', unique=True)
    slug            =   models.SlugField(null=True, blank=False, verbose_name="Slug", unique=True)

    code            =   models.CharField(max_length=15, null=True, blank=False, verbose_name='Code', unique=True, help_text="Max 10 characters")

    description     =   models.TextField(null=True, blank=True, verbose_name="Description", help_text="Write in some lines more info about this category")

    # SEO
    seo_keywords        =   models.CharField(max_length=300, blank=True, null=True, verbose_name='Keywords', help_text="Add keyword using a comma (e.g. 'politics,business,finance')")
    seo_description     =   models.TextField(max_length=350, null=True, blank=True, verbose_name="Description", help_text="300 character limit")

    # Insights
    created_at          =   models.DateTimeField(auto_now_add=True, null=True, blank=False, verbose_name="Created Date")
    last_edit           =   models.DateTimeField(auto_now=True, null=True, blank=False, verbose_name="Updated On")

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        db_table = "courses_category"

    def __str__(self):
        return f"{self.name}"

#--------#
#  Tags  #
#--------#
class Tags(models.Model):

    # Info
    name                =   models.CharField(max_length=200, null=True, blank=False, verbose_name='Name', unique=True)
    slug                =   models.SlugField(null=True, blank=False, verbose_name="Slug", unique=True)

    # Insights
    created_at          =   models.DateTimeField(auto_now_add=True, null=True, blank=False, verbose_name="Created Date")
    last_edit           =   models.DateTimeField(auto_now=True, null=True, blank=False, verbose_name="Updated On")

    class Meta:
        verbose_name = 'Tags'
        verbose_name_plural = 'Tags'
        db_table = "courses_tags"

    def __str__(self):
        return f"{self.name}"

#---------#
# Courses #
#---------#
class Courses(models.Model):

    # Bool
    yes = 'Yes'
    no = 'No'
    BOOL_CHOICES = [
        (yes, yes),
        (no, no),
    ]
    # Level
    beginner = 'Beginner'
    intermediate = 'Intermediate'
    advanced = 'Advanced'
    professional = 'Professional'
    SET_LEVEL_CHOICES = [
        (beginner, beginner),
        (intermediate, intermediate),
        (advanced, advanced),
        (professional, professional),
    ]
    # Language
    fr = 'French'
    en = 'English'
    ht = 'Haitian creole'
    SET_LANG_CHOICES = [
        (fr, fr),
        (en, en),
        (ht, ht),
    ]

    # Path to media
    def path_and_rename(instance, filename):
        master_path = 'courses/covers'
        ext = filename.split('.')[-1]
        # get filename
        path = f"{master_path}/{instance.slug}/"
        path_file_name = f"{instance.slug}-on-techonlearning-{uuid.uuid4()}"
        filename = '{}/{}.{}'.format(path, path_file_name, ext)
        # return the whole path to the file
        return filename

    # UUID
    uuid            =   models.UUIDField(primary_key=False, unique=True, blank=False, null=True, default=uuid.uuid4, editable=False)

    # Info
    name            =   models.CharField(max_length=300, null=True, blank=False, verbose_name='Name', unique=True)
    slug            =   models.SlugField(null=True, blank=False, verbose_name="Slug", unique=True)

    teacher         =   models.ForeignKey(Profile, related_name='courses_teacher_rel', on_delete=models.CASCADE, null=True, blank=False, verbose_name='Teacher')
    category        =   models.ForeignKey(Category, related_name='courses_category_rel', on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Category')
    tags            =   models.ManyToManyField(Tags, related_name="courses_tags_rel", blank=True, verbose_name="Tags", help_text="Add some tags")

    introduction    =   models.TextField(null=True, blank=True, verbose_name="Introduction", help_text="Write in some lines more info about this course")
    description     =   tinymce_models.HTMLField(null=True, blank=False, verbose_name="Description", help_text="Start writing about this course...")

    location        =   models.CharField(max_length=200, null=True, blank=False, verbose_name='Location', unique=True)
    location_map    =   models.TextField(max_length=1000, null=True, blank=False, verbose_name='Location map', unique=True, help_text="Insert the google map iFrame code")

    price           =   models.IntegerField(null=True, blank=True, verbose_name="Price", help_text="Price in HTG")

    # Timeframe
    start_date      =   models.DateField(auto_now_add=False, null=True, blank=False, unique=False, verbose_name="Start date")
    end_date        =   models.DateField(auto_now_add=False, null=True, blank=False, unique=False, verbose_name="End date")

    # cover
    cover                     =   models.ImageField(upload_to=path_and_rename, null=True, default=None, blank=False, verbose_name='Cover')
    cover_thumb               =   ImageSpecField(source='cover',
                                    format='JPEG',
                                    options={'quality': 30})
    cover_thumb_small           =   ImageSpecField(source='cover',
                                    processors=[ResizeToFill(600, 400)],
                                    format='JPEG',
                                    options={'quality': 50})
    cover_thumb_small_hd           =   ImageSpecField(source='cover',
                                    processors=[ResizeToFill(600, 400)],
                                    format='JPEG',
                                    options={'quality': 100})
    og_card                     =   ImageSpecField(source='cover',
                                    processors=[ResizeToFill(1200, 630)],
                                    format='JPEG',
                                    options={'quality': 50})

    # Courses Includes
    set_certificate         =   models.CharField(max_length=150, choices=BOOL_CHOICES, default=no, verbose_name="Certificate")
    set_level               =   models.CharField(max_length=150, choices=SET_LEVEL_CHOICES, default=beginner, verbose_name="Skill level")
    set_language            =   models.CharField(max_length=150, choices=SET_LANG_CHOICES, default=ht, verbose_name="Language")

    # Status
    status              =   models.CharField(max_length=100, choices=STATUS, default=draft, verbose_name="Status")

    # SEO
    seo_keywords        =   models.CharField(max_length=300, blank=True, null=True, verbose_name='Keywords', help_text="Add keyword using a comma (e.g. 'politics,business,finance')")
    seo_description     =   models.TextField(max_length=350, null=True, blank=True, verbose_name="Description", help_text="300 character limit")

    # Insights
    created_at          =   models.DateTimeField(auto_now_add=True, null=True, blank=False, verbose_name="Created Date")
    last_edit           =   models.DateTimeField(auto_now=True, null=True, blank=False, verbose_name="Updated On")

    def get_absolute_url(self):
        return reverse("courses:detail", args=[str(self.slug)])

    class Meta:
        verbose_name = 'Course'
        verbose_name_plural = 'Courses'
        db_table = "courses_cs"

    def __str__(self):
        return f"{self.name}"

#---------#
#  Guide  #
#---------#
class Guide(models.Model):
    # Link
    course           =   models.ForeignKey(Courses, related_name='courses_guide_rel', on_delete=models.SET_NULL, null=True, blank=False, verbose_name='Course')

    # Info
    name                =   models.CharField(max_length=400, null=True, blank=False, verbose_name='Guide', unique=True, help_text="What people will learn in this course")

    class Meta:
        verbose_name = 'Guide'
        verbose_name_plural = 'Guides'
        db_table = "courses_guides"

    def __str__(self):
        return f"{self.name}"