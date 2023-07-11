from django import forms
from .models import BlogPost, Comments


# creating comments form
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['comment']
