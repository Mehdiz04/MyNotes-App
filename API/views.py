from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView , CreateAPIView , RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.status import HTTP_201_CREATED , HTTP_400_BAD_REQUEST
from rest_framework_simplejwt.tokens import RefreshToken
from MyNotesApp.models import Note
from .serializers import NoteSerializer , UserRegistrationSerializer
from django.contrib.auth.models import User

# Create your views here.

@api_view(['GET'])
def routes(request):
    routes = [
        {
            'route':'http://127.0.0.1:8000/api/routes/',
            'methods':'GET',
            'doc':'to get all the available routes',
        } ,

        {
            'route':'http://127.0.0.1:8000/api/token/refresh/',
            'methods':'POST',
            'doc':'send user username/password get refresh and access token',
        } ,
        {
            'route':'http://127.0.0.1:8000/api/token/',
            'methods':'POST',
            'doc':'send refresh token get new access token',
        } ,
        {
            'route':'http://127.0.0.1:8000/api/register/',
            'methods':'POST',
            'doc':'post username/password -> create a new user',
        } ,
        {
            'route':'http://127.0.0.1:8000/api/notes/',
            'methods':'GET',
            'doc':'get all the notes written by that user',
        } ,
        {
            'route':'http://127.0.0.1:8000/api/create-note/',
            'methods':'POST (post data -> Title , content)',
            'doc':'save a new note to the database, the author field will be automatically set to the request user',
        } ,
        {
            'route':'http://127.0.0.1:8000/api/note/<int:pk>/',
            'methods':'PUT (update) , DELETE (delete) , GET',
            'doc':'get a detail view for a note and u can update,delete it',
        } ,
        {
            'route':'http://127.0.0.1:8000/api/blacklist-token/',
            'methods':'POST -> post refresh token',
            'doc':'blacklsit that refresh token',
        } ,
    ]

    return Response(routes)


class NotesListView(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = NoteSerializer
    
    def get_queryset(self):
        return Note.objects.filter(author=self.request.user)
    

class CreateNote(CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = NoteSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class NoteDetail(RetrieveUpdateDestroyAPIView):
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Note.objects.filter(author=self.request.user)
    

class Register(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data = request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({"message": "User registered successfully"}, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
    

@api_view(['POST'])
def blacklistToken(request):
    refresh_token = RefreshToken(request.data['refresh'])
    refresh_token.blacklist()
    return Response({"token":"refresh token blacklisted"})