from django import forms
from django.forms import ModelForm
from .models import *


# Форма добавление статей
class AddArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content', 'image']



