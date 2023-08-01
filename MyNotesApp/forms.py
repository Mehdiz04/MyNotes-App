from django import forms
from .models import Note

class addNoteForm(forms.Form):
    Title = forms.CharField(max_length=40)
    content = forms.CharField(widget=forms.Textarea(attrs={'rows': 10, 'cols': 80, 'maxlength': 2000}))
    