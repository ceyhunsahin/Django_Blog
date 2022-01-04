from django import forms
from .models import Post, Comment, Category

class PostForm(forms.ModelForm):
    status = forms.ChoiceField(choices=Post.OPTIONS)
    category = forms.ModelChoiceField(
                queryset = Category.objects.all(), empty_label="Select")

    class Meta:
        model = Post
        field = ['title', 'content', 'category', 'status', 'image']

class CommentForm(forms.ModelForm):
    class Meta :
        model = Comment
        fields = ['content']