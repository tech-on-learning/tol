from django.contrib import admin
from .models import Profile

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user','title',)
    search_fields = ('user','bio',)
    readonly_fields = ('uuid',)

    filter_horizontal = ()
    fieldsets = (
        ('Account', {'fields':('user',)}),
        ('Personal Info', {'fields':('title','bio','avatar',)}),
        ('Social accounts', {'fields':('facebook','twitter','instagram','linkedin',)}),
    )

# Register your models here.
admin.site.register(Profile, ProfileAdmin)