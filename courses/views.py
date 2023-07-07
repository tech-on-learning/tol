from django.shortcuts import render, get_object_or_404, redirect
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
    # OBJ
    all_courses_obj = Courses.objects.filter(status='Published').all()
    count_all_courses_obj  =   all_courses_obj.count() 

    # Website Settings
    js_header = True
    title = "Our Courses"

    # SEO
    seo_description = _("")
    seo_keywords = _("")

    context = {
        "all_courses_obj":all_courses_obj,
        "count_all_courses_obj":count_all_courses_obj,

        "seo_description":seo_description,
        "seo_keywords":seo_keywords,

        "title":title,

        "js_header":js_header,
    }

    return render(request, 'courses/index.html', context)

##############################################
# DETAIL
def detail(request, course_slug):
    # obj
    course_detail_obj = get_object_or_404(Courses, slug=course_slug)
    # obj / Final
    page_detail=course_detail_obj

    # OBJ / Related
    related_courses_obj = Courses.objects.exclude(slug=course_slug).filter(status='Published').filter(tags__in=page_detail.tags.all()).distinct()[:3]
    related_courses_obj_sum_count = related_courses_obj.count()

    # OBJ / Count
    count_teacher_courses=page_detail.teacher.courses_teacher_rel.filter(status='Published').all().count()

    # SEO
    seo_description = _("")
    seo_keywords = _("")

    # Website Settings
    js_header = True
    title = "Our Courses"

    context = {
        "seo_description":seo_description,
        "seo_keywords":seo_keywords,

        "course_detail_obj":course_detail_obj,
        "page_detail":page_detail,

        "related_courses_obj":related_courses_obj,
        "related_courses_obj_sum_count":related_courses_obj_sum_count,

        "count_teacher_courses":count_teacher_courses,

        "title":title,

        "js_header":js_header,
    }

    return render(request, 'courses/detail.html', context)
