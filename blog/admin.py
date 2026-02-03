from django.contrib import admin
from django.contrib import admin
from blog.models import Category, Maqola, Comment, Like

admin.site.register(Category)
admin.site.register(Maqola)
admin.site.register(Comment)
admin.site.register(Like)