from django import forms 
from blog.models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'image', 'category', 'summary', 'content', 'draft']
        widgets = {
            'title': forms.TextInput(attrs={"placeholder": "Title", "autofocus": "autofocus"}),
            'summary': forms.TextInput(attrs={"placeholder": "Summary"}),
            'content': forms.Textarea(attrs={"placeholder": "Content", "rows": "4"}),
        }