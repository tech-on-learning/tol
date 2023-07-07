from django.shortcuts import render, redirect
from django.http import HttpResponse

# Import Messages
from django.contrib import messages
from django.template.loader import get_template, render_to_string

# Import Email Backend
from django.core.mail import EmailMessage, EmailMultiAlternatives

# Import Settings
from django.conf import settings

# Import models

# Import Forms

# Counts
from django.db.models import Count

# Anti SPAM
from honeypot.decorators import check_honeypot

# Internationalization
from django.utils.translation import gettext as _

##############################################
# Contact
def index(request):
    seo_description = _("")
    seo_keywords = _("")

    # Website Settings
    js_header = True
    title = "Our Courses"

    context = {
        "seo_description":seo_description,
        "seo_keywords":seo_keywords,
        "title":title,

        "js_header":js_header,
    }

    return render(request, 'contact/index.html', context)


##############################################
# Student
def student(request):
    seo_description = _("")
    seo_keywords = _("")

    # Website Settings
    js_header = True
    title = "Become a student"

    context = {
        "seo_description":seo_description,
        "seo_keywords":seo_keywords,
        "title":title,

        "js_header":js_header,
    }

    return render(request, 'contact/with_form.html', context)

##############################################
# Teacher
def teacher(request):
    seo_description = _("")
    seo_keywords = _("")

    # Website Settings
    js_header = True
    title = "Become a teacher"

    context = {
        "seo_description":seo_description,
        "seo_keywords":seo_keywords,
        "title":title,

        "js_header":js_header,
    }

    return render(request, 'contact/with_form.html', context)