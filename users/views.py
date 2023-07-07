from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse

# Import Models
from users.models import Profile
from courses.models import Courses

# Model User
from django.contrib.auth.models import User

##############################################

def index(request, url_slug):
    user_obj = get_object_or_404(User, username=url_slug)

    # obj / Final
    page_detail=user_obj

    if user_obj.get_full_name():
        title = f"{user_obj.get_full_name()}"
    else:
        title = f"{user_obj.username}"

    context = {
        "title": title,

        "page_detail":page_detail,
        "user_obj": user_obj,
    }
    return render(request, 'users/index.html', context)

##############################################