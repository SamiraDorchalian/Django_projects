# from django.forms import Form, ModelForm
from django import forms

from .models import Post

class NewPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'text', 'auther', 'status']
