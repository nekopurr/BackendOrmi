# blog/forms.py
from django import forms
from .models import Post, Comment, HashTag

# Form: html에 있는 form 태그
# Model Form: model을 사용하는 form
class PostForm(forms.ModelForm):
    
    class Meta:
        model = Post
        fields = ['title', 'content']


class CommentForm(forms.ModelForm):
    
    class Meta:
        model = Comment
        fields = ['content'] # field (사용자에게 보여주는 input 내용)
        widgets = {
            'content': forms.Textarea(attrs={'rows': '3', 'cols':'35'})
        }


class HashTagForm(forms.ModelForm):
    
    class Meta:
        model = HashTag
        fields = ['name'] # 사용자에게 입력받아야 하는 내용