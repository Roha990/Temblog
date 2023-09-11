from django.contrib import admin
from .models import *


# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ("username", "first_name", "last_name")
    search_fields = ("username", "first_name", "last_name")


class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title", "published", "user")
    search_fields = ("title", "content", "user")


admin.site.register(Article, ArticleAdmin)
admin.site.register(User, UserAdmin)
