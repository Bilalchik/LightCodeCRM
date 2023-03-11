from django.contrib import admin
from django.conf.urls import handler404, handler500
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('landing.urls')),
    path('srm/', include('srm.urls')),
    path('account/', include('account.urls')),
    path('classroom/', include('classroom.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'landing.views.error_404'
handler500 = 'landing.views.error_500'

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
