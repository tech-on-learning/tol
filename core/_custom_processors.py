from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect

# Models

# Forms

# Anti SPAM
from honeypot.decorators import check_honeypot

# Import Messages
from django.contrib import messages
from django.template.loader import get_template, render_to_string

# Import Email Backend
from django.core.mail import EmailMessage, EmailMultiAlternatives

# Import Settings
from django.conf import settings 
from django.conf.urls.static import static

# Counts
from django.db.models import Count

##############################################
# Contact