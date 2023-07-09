from django.contrib import admin

# Models
from .models import Message

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

# Register your models here.
admin.site.register(Message, MessageAdmin)