from django import forms
from django.forms import ModelForm
from .models import Stories, Comment

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['comment_text', 'user']
