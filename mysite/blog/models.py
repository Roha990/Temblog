import urllib
from io import StringIO

from PIL import Image
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.forms import forms
from django.http import request
from django.core.files import File
import os
from django.forms import ModelForm


# Create your models here.

# Модель пользователя в БД
class User(AbstractUser):
    username = models.CharField(max_length=20, unique=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    USERNAME_FIELD = "username"

    def create_user(self, username, first_name, last_name, email, password):
        self.username = username
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.set_password(password)
        self.save()

    def __str__(self):
        return self.username


# Модель статьи в БД
class Article(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название статьи')
    content = models.TextField(null=True, blank=True, verbose_name='Текст статьи')
    published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Опубликовано')
    image = models.ImageField(null=True, blank=True, upload_to="images/", verbose_name='Изображение')
    user = models.ForeignKey('User', on_delete=models.PROTECT)

    def add(self, title, content, image, user_pk):
        self.title = title
        self.content = content
        self.image = image
        self.user_id = user_pk
        self.save()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Статьи'
        verbose_name = 'Статья'
        ordering = ['-published']


