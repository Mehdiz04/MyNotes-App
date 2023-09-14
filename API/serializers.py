from rest_framework import serializers
from django.contrib.auth.models import User
from MyNotesApp.models import Note

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ('id' , 'Title' , 'content')

class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username' , 'password')
        extra_kwargs = {'password':{'write_only': True}}

    def save(self, **kwargs):
        user = User(username=self.validated_data['username'])
        password = self.validated_data['password']

        if (len(password) < 8) or (user.username in password):
            raise serializers.ValidationError({"password": "Password must be at least 8 characters long and not contain username"})
        
        user.set_password(password)
        user.save()
        return user