from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path, include

from shop.views import index


urlpatterns = [
    path('', index, name="index"),
    path('admin/', admin.site.urls),
    path('shop/', include('shop.urls')),
    path('auth/', include('core.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
