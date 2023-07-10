from django.contrib import admin
from django.urls import path, include, re_path

from django.conf import settings 
from django.conf.urls.static import static

from django.views.static import serve

# Internationalisation
from django.conf.urls.i18n import i18n_patterns
from django.utils.translation import gettext as _

admin.site.site_header = 'Tech On Learning'
admin.site.site_title = 'Tech On Learning Dashboard'

urlpatterns = i18n_patterns(
    # Default Lang
    prefix_default_language=False,
)
urlpatterns += [
    path('admin/', admin.site.urls),

    # Company Dirs
    path('courses/', include('courses.urls')),
    # Users
    path('@', include('users.urls')),

    # Text Editor
    path('tinymce/', include('tinymce.urls')),
    # Hit-count
    path('hitcount/', include('hitcount.urls', namespace='hitcount')),

    # Root Paths
    path('', include('company.urls')),
    path('contact/', include('contact.urls', namespace='contact_url')),
    # Core
    path('', include('core.urls')),
]
urlpatterns += [
    re_path(r'^media/(?P<path>.*)$', serve, {
        'document_root': settings.MEDIA_ROOT,
    }),
    re_path(r'^static/(?P<path>.*)$', serve, {
        'document_root': settings.MEDIA_ROOT,
    }),
]

# Error handler
handler400 = "core.views.error_400"
handler403 = "core.views.error_403"
handler404 = "core.views.error_404"
handler500 = "core.views.error_500"