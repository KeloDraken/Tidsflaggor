"""
URL configuration for src project.
"""

from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.contrib.auth.models import Group

from django.urls import path

urlpatterns = (
    [
        path("admin/", admin.site.urls),
    ]
    + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
)

admin.site.site_header = "Tidsflaggor Site Admin"
admin.site.site_title = "Tidsflaggor Site Admin"

admin.site.unregister(Group)
