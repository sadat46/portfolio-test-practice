from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),    
    path('', include('sadat.urls')),# if blank, it will go to sadat url    
    path('', include('ashik.urls')),
    # path('home/', include('sadat.urls')),# if /home/ , it will go to sadat url
    ]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)