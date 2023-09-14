from django.urls import path 
from rest_framework_simplejwt.views import TokenObtainPairView , TokenRefreshView
from . import views

urlpatterns = [
    path('routes/' , views.routes , name='routes'),
    #authentication
    path('token/refresh/' , TokenObtainPairView.as_view() , name='token-obtain-pair'),
    path('token/' , TokenRefreshView.as_view() , name='token-refresh'),
    #register
    path('register/' , views.Register.as_view() , name='register'),
    #api endpoints
    path('notes/' , views.NotesListView.as_view() , name='notes-list'),
    path('create-note/' , views.CreateNote.as_view() , name='create-note'),
    path('note/<int:pk>' , views.NoteDetail.as_view() , name='note-detail'),
    #blacklist token / logout
    path('blacklist-token/' , views.blacklistToken , name='blacklist-token'),
]
