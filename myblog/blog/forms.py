from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):
    post_anon = forms.BooleanField(required=False, label="Post Anonymously")

    class Meta:
        model = Post
        fields = ['title', 'content', 'post_anon', 'image']

class CommentForm(forms.ModelForm):
    post_anon = forms.BooleanField(required=False, label="Post Anonymously")

    class Meta:
        model = Comment
        fields = ['content', 'post_anon']