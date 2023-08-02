
from django.contrib import admin
from django.urls import path , include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('' , home),
    path('blog/<slug:url>' , post),
    path('category/<slug:url>' , display_post),
    
    
]
