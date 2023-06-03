from django import forms
from .models import Blog, Category


class BlogForm(forms.ModelForm):
    published_at = forms.DateField(widget=forms.SelectDateWidget())

    class Meta:
        model = Blog
        fields = ['title', 'description',
                  'image', 'category', 'published_at']
