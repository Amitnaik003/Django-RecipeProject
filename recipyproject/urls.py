from django.contrib import admin
from django.urls import path 
from vege.views import *
from django.conf import settings 
from django.conf.urls.static import static 
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
  
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', receipes, name='receipes'),  # root URL and main recipe list
    path('delete_receipe/<int:id>/', delete_receipe, name='delete_receipe'),
    path('update_receipe/<int:id>/', update_receipe, name='update_receipe'),
    path('login/', login_page, name='login_page'),
    path('logout/', logout_page, name='logout'),
    path('register/', register_page, name='register_page'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()

