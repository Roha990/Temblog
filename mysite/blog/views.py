import random

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import CreateView

from .functions import *
from .models import *
from .forms import *


# Create your views here.

# Вьюха для того, чтобы пользователь мог попасть на свою страницу при клике на ссылку "Мой блог"
def my_page(request):
    return redirect(index, request.user.id)


# После полного просмотра статьи, пользователь захотел ознакомится с другими статьями данного автора. Эта вьюха ведет
# пользователя к автору статьи
def back(request):
    return redirect(f"../id{request.user.id}/")


# Просмотр блога пользователя
def index(request, user_profile_id):
    try:
        user = User.objects.get(pk=user_profile_id)
        articles = Article.objects.filter(user_id=user_profile_id)
    except:
        articles = None
        user = None
    context = {"articles": articles, "user": user}
    return render(request, "blog/index.html", context)


# Просмотр полного текста статьи
def get_article(request, article_id):
    current_article = Article.objects.get(pk=article_id)
    current_user = User.objects.get(pk=current_article.user_id)
    context = {"current_article": current_article, "current_user": current_user}
    return render(request, "blog/article.html", context)


# Регистрация
def register(request):
    if not request.user.is_authenticated:
        if request.method == "GET":
            return render(request, "blog/registr.html")
        else:
            data = request.POST
            username = data["username"]
            first_name = data["first_name"]
            last_name = data["last_name"]
            email = data["email"]
            password1, password2 = data["password1"], data["password2"]
            if username is None or first_name is None or last_name is None or email is None or password1 is None or password2 is None:
                return HttpResponse("<h3>Заполните все поля</h3>")
            elif password1 != password2:
                return HttpResponse("<h3>Пароли должны совпадать</h3>")
            else:
                newuser = User()
                newuser.create_user(username, first_name, last_name, email, password1)
                return redirect("../auth/")


# Авторизация
def auth(request):
    if not request.user.is_authenticated:
        if request.method == "GET":
            return render(request, "blog/auth.html")
        else:
            data = request.POST
            try:
                user = authenticate(request, username=data['username'], password=data['password'])
                if user is None:
                    return HttpResponse("Такой пользователь не найден либо пароли не совпадают")
                login(request, user)
                user_profile = User.objects.get(username=data['username'])
                return redirect(f"../id{user_profile.pk}")
            except KeyError:
                return HttpResponse("<h3>Заполните все поля</h3>")


# Выход из личного кабинета
def logout_page(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect("../auth/")


# Добавление статей. Чтобы добавить статью нужно быть авторизованным
@login_required
def add_article(request):
    if request.method == "GET":
        form = AddArticleForm()
        return render(request, "blog/add_article.html", {"form": form})
    if request.method == "POST":
        model_form = AddArticleForm(request.POST, request.FILES)
        if model_form.is_valid():
            form = model_form.save(commit=False)
            form.user_id = request.user.id
            form.save()
            return redirect(f"../id{request.user.id}")


# Список всех существующих блогов
def blog_list(request):
    blogs = User.objects.all()
    context = {"blogs": blogs}
    return render(request, "blog/blog_list.html", context)
