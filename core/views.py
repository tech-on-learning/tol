from django.shortcuts import render, redirect
from django.http import HttpResponse

# Import Messages
from django.contrib import messages
from django.template.loader import get_template, render_to_string

# Import Email Backend
from django.core.mail import EmailMessage, EmailMultiAlternatives

# Import Settings
from django.conf import settings

# Internationalization
from django.utils.translation import gettext as _
from django.utils.translation import get_language, activate, get_language_info


# Error pages
##############################################

def error_400(request, exception):
    title = _("Bad request")

    context = {
        "title":title,
    }
    return render(request, 'errors/400.html', context, status=400)

def error_403(request, exception):
    title = _("HTTP Forbidden")

    context = {
        "title":title,
    }
    return render(request, 'errors/403.html', context, status=403)

def error_404(request, exception):
    title = _("Page not found")

    context = {
        "title":title,
    }
    return render(request, 'errors/404.html', context, status=404)

def error_500(request, exception=True):
    title = _("Server error")

    context = {
        "title":title,
    }
    return render(request, 'errors/500.html', context, status=500)