from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('' , views.home , name='home'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/' , views.register , name='register'),
    path('NewNote/' , views.add_note , name = 'add_note'),
    path('note/<int:noteid>' , views.noteview , name = 'note'),
    path('delete_note/<int:noteid>' , views.delete_noteview , name='delete_note'),
    path('update_note/<int:noteid>' , views.update_noteview , name='update_note')
]