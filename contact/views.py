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
from contact.forms import MessageForm

# Counts
from django.db.models import Count

# Anti SPAM
from honeypot.decorators import check_honeypot

# Internationalization
from django.utils.translation import gettext as _

##############################################
# Contact
@check_honeypot(field_name="check_name")
def index(request):

    seo_description = _("")
    seo_keywords = _("")

    title = "Contact"

    if request.method == "POST":
        form = MessageForm(request.POST or None)

        # If form is valid
        if form.is_valid():

            # Before Validation
            msg_obj = form.save(commit=False)

            # Send the email
            first_name      =   request.POST.get('first_name')
            last_name       =   request.POST.get('last_name')
            subject         =   request.POST.get('subject')
            email           =   request.POST.get('email')
            message         =   request.POST.get('message')
            context_emails  =   {
                "first_name":first_name,
                "last_name":last_name,
                "subject":subject,
                "email":email,
                "message":message,
            }
            html_message    =   render_to_string('_emails/messages/contact.html', context_emails)

            from_email = f"Tech on Learning (website) <{settings.EMAIL_HOST_USER}>"
            to = settings.EMAIL_RECIPIENT_LIST

            send_msg = EmailMultiAlternatives(
                subject, 
                html_message,
                from_email, 
                to,
                reply_to = [email],
            )
            send_msg.attach_alternative(html_message, "text/html")
            send_msg.content_subtype = "html"

            # Send 
            send_msg.send()

            # Save msg Obj
            msg_obj.save()

            # Messages
            messages.success(request, "Your message has been sent successfully!")
            form = MessageForm(None)

        else:
            messages.error(request, "There was an error while trying to send your message")

    else:
        form = MessageForm(None)

    context = {
        "title":title,
        "form": form,
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