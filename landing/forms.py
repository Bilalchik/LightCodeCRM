from django import forms
from .models import Section, Article
from ckeditor.widgets import CKEditorWidget


class SectionForm(forms.ModelForm):

    class Meta:
        model = Section
        fields = ['title', 'slug', 'id_section']


class ArticleForm(forms.ModelForm):
    body = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Article
        fields = ['topic_name', 'slug', 'section', 'body']


