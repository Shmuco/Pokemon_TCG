from django import forms
from .models import *

class PostForm(forms.ModelForm):
    class Meta:
        Model = Post
        fields = '__all__'

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ('creator',
                    'post',)
       
        # fields = '__all__'