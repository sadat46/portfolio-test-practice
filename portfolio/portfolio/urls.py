from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),    
    path('', include('sadat.urls')),# if blank, it will go to sadat url    
    path('', include('ashik.urls')),
    # path('home/', include('sadat.urls')),# if /home/ , it will go to sadat url
    ]
