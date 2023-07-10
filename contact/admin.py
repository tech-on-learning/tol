from django.contrib import admin

# Models
from .models import Message, Student, Teacher

class MessageAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name','email','subject',)
    readonly_fields = ('date',)
    search_fields = ('first_name','last_name','email','message',)
    list_filter = ('date',)

    fieldsets = (
        ('Info', {'fields':('first_name','last_name','email',)}),
        ('subject', {'fields':('subject',)}),
        ('Message', {'fields':('message',)}),
        ('Insights', {'fields':('date',)}),
    )

class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name','email',)
    readonly_fields = ('date',)
    search_fields = ('first_name','last_name','email','course','message',)
    list_filter = ('date',)

    fieldsets = (
        ('Personal Info', {'fields':('first_name','last_name','email',)}),
        ('Course', {'fields':('course',)}),
        ('Q&A', {'fields':('q_price','set_schedule','q_laptop','q_wish','q_hearing_us','q_certificate',)}),
        ('Message', {'fields':('message',)}),
        ('Insights', {'fields':('date',)}),
    )

class TeacherAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name','email',)
    readonly_fields = ('date',)
    search_fields = ('first_name','last_name','email','course','message',)
    list_filter = ('date','set_education_level',)

    fieldsets = (
        ('Personal Info', {'fields':('first_name','last_name','email','set_education_level',)}),
        ('Course', {'fields':('course',)}),
        ('Message', {'fields':('message',)}),
        ('Insights', {'fields':('date',)}),
    )

# Register your models here.
admin.site.register(Message, MessageAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Teacher, TeacherAdmin)