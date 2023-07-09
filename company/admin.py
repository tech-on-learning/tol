from django.contrib import admin

# Models
from .models import Testimonials

class TestimonialsAdmin(admin.ModelAdmin):
    list_display = ('name',)
    readonly_fields = ('created_at','last_edit',)

    fieldsets = (
        ('Info', {'fields':('name','title','avatar',)}),
        ('Testimonials', {'fields':('message',)}),
        ('Insights', {'fields':('created_at','last_edit',)}),
    )

# Register your models here.
admin.site.register(Testimonials, TestimonialsAdmin)