from django import forms
from .models import Post, Comments

class CreatePost(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'content')

class CommentCreate(forms.ModelForm):

    class Meta:
        model = Comments
        fields = ('context', )
