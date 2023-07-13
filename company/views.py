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
from courses.models import Category, Tags, Courses, Guide
from users.models import Profile
from company.models import Testimonials

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
    # OBJ / Latest Courses
    latest_courses_obj = Courses.objects.filter(status='Published').order_by('-created_at').all()[:3]
    latest_courses_obj_1st = latest_courses_obj[:1]
    # OBJ / Courses
    courses_obj = Courses.objects.all()
    # OBJ / Teachers
    teacher_obj = Profile.objects.all()
    # OBJ / Testimonials
    testimonials_obj = Testimonials.objects.order_by('-created_at').all()

    count_teacher_obj = teacher_obj.count()
    count_courses_obj = courses_obj.count()

    seo_description = _("Invest in your future with Tech On Learning and acquire the new skills necessary to take your career to the next level")
    seo_keywords = _("tech on learning, tech, online courses, excel, powerbi, teachonlearn")

    # Website Settings
    js_header = True

    context = {
        "latest_courses_obj":latest_courses_obj,
        "latest_courses_obj_1st":latest_courses_obj_1st,

        "teacher_obj":teacher_obj,
        "testimonials_obj":testimonials_obj,

        "count_teacher_obj":count_teacher_obj,
        "count_courses_obj":count_courses_obj,

        "seo_description":seo_description,
        "seo_keywords":seo_keywords,

        "js_header":js_header,
    }

    return render(request, 'company/home.html', context)
