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
# HOME
def index(request):
    seo_description = _("We use the power of marketing and communication to bring your project to life")
    seo_keywords = _("graphic designer, digital marketing, haitian designer")

    # Website Settings
    js_header = True

    context = {
        "seo_description":seo_description,
        "seo_keywords":seo_keywords,

        "js_header":js_header,
    }

    return render(request, 'company/home.html', context)
