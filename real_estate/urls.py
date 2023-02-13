from django.conf import settings
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static

urlpatterns = [
    path("superuser/", admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = "Custom bookstore admin"
admin.site.site_title = "Custom bookstore admin site"
admin.site.index_title = "Custom Bookstore Admin"
