from django.contrib import admin
from django.urls import path, include
from django.conf import settings  # Import Django settings module
from django.conf.urls.static import static  # Import the static function

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('movieapp.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
