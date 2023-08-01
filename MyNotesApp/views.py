from django.shortcuts import render , redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import addNoteForm
from .models import Note
# Create your views here.

@login_required
def home(request):
    context = {'Notes':Note.objects.filter(author=request.user)}
    return render(request , 'home.html' , context)


def register(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('login')
        else:
            user_name = request.POST['username']
            if User.objects.filter(username=user_name).exists():
                messages.error(request , f'username ({user_name}) already exists')
                return redirect('register')
            else:
                messages.error(request , f'invalid password')
                return redirect('register') 

    return render(request , 'register.html' , {'form':form})


@login_required
def add_note(request):
    if request.method == 'POST':
        note = Note()
        note.Title = request.POST['Title']
        note.content = request.POST['content']
        note.author = request.user
        note.save()
        messages.success(request, 'Note created')
        return redirect('home')

    context = {'form':addNoteForm}
    return render(request , 'add_note.html' , context)

@login_required
def noteview(request , noteid):
    note = Note.objects.get(id=noteid)
    if not note or note.author != request.user:
        messages.warning(request , 'invalid request')
        return redirect('home')
    else:
        return render(request , 'note.html' , {'note':note})
    

@login_required
def delete_noteview(request , noteid):
    note = Note.objects.get(id=noteid)
    if not note or note.author != request.user:
        messages.warning(request , 'invalid request')
        return redirect('home')
    else:
        note.delete()
        messages.success(request , 'Note deleted!')
        return redirect('home')
    

@login_required
def update_noteview(request , noteid):
    note = Note.objects.get(id=noteid)
    if not note or note.author != request.user:
        messages.warning(request , 'invalid request')
        return redirect('home')
    else:
        if request.method == 'POST':
            note.Title = request.POST['Title']
            note.content = request.POST['content']
            note.save()
            messages.success(request , 'note updated!')
            return redirect('home')
        
        form = addNoteForm(initial={'Title': note.Title , 'content': note.content})
        return render(request , 'update_note.html' , {'form':form})