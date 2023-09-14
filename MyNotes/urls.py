from django.contrib import admin
from MyNotesApp import urls as main_urls
from API import urls as API_urls
from django.urls import path , include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(main_urls)),
    path('api/' , include(API_urls)),
]
