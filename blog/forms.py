from django import forms
from .models import Blog

class BlogForm(forms.ModelForm):

    class Meta:
        model = Blog
        fields = ['title', 'category', 'thumbnail', 'summary', 'content', 'is_draft']

class BlogCategoryForm(forms.Form):
    CATEGORY_CHOICES = (
        ('All', 'All'),
        ('Mental Health', 'Mental Health'),
        ('Heart Disease', 'Heart Disease'),
        ('Covid19', 'Covid19'),
        ('Immunization', 'Immunization'),
    )
    category = forms.ChoiceField(choices = CATEGORY_CHOICES, required = False)
    class Meta:
        fields = ['category']
