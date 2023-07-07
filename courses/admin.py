from django.contrib import admin

# Models
from courses.models import Category, Tags, Courses, Guide

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    prepopulated_fields = {"slug": ("name",)}
    list_filter = ('created_at','last_edit',)
    readonly_fields = ('created_at','last_edit',)
    search_fields = ('name',)

    fieldsets = (
        ('Info', {'fields':('name','slug','description',)}),
        ('SEO', {'fields':('seo_keywords','seo_description',)}),
        ('Insights', {'fields':('created_at','last_edit',)}),
    )

class TagsAdmin(admin.ModelAdmin):
    list_display = ('name',)
    prepopulated_fields = {"slug": ("name",)}
    list_filter = ('created_at','last_edit',)
    readonly_fields = ('created_at','last_edit',)
    search_fields = ('name',)

    fieldsets = (
        ('Info', {'fields':('name','slug',)}),
        ('Insights', {'fields':('created_at','last_edit',)}),
    )

class courses_guide_Inline(admin.StackedInline):
    model = Guide
    fields = ["name",]
    extra = 0

class CoursesAdmin(admin.ModelAdmin):
    inlines = [courses_guide_Inline]
    list_display = ('name','teacher','category','price','start_date','end_date',)
    list_filter = ('created_at','last_edit','status','set_certificate','set_level','set_language',)
    readonly_fields = ('uuid','created_at','last_edit',)
    search_fields = ('name','teacher','category','description',)
    prepopulated_fields = {"slug": ("name",)}

    fieldsets = (
        ('UUID', {'fields':('uuid',)}),
        ('Info', {'fields':('name','slug','teacher','category','tags','price',)}),
        ('Description', {'fields':('introduction','description',)}),
        ('TimeFrame', {'fields':('start_date','end_date',)}),
        ('Cover picture', {'fields':('cover',)}),
        ('This Course Includes', {'fields':('set_certificate','set_level','set_language',)}),
        ('SEO', {'fields':('seo_keywords','seo_description',)}),
        ('Insights', {'fields':('created_at','last_edit',)}),
        ('Status', {'fields':('status',)}),
    )

class GuideAdmin(admin.ModelAdmin):
    list_display = ('name','course',)
    search_fields = ('name','course',)

    fieldsets = (
        ('Info', {'fields':('name',)}),
        ('Course', {'fields':('course',)}),
    )

# Register your models here.
admin.site.register(Category, CategoryAdmin)
admin.site.register(Tags, TagsAdmin)
admin.site.register(Courses, CoursesAdmin)
admin.site.register(Guide, GuideAdmin)