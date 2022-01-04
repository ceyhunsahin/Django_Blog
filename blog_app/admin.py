from django.contrib import admin
from .models import Category, Post, Comment, PostView, Like

admin.site.register(Category)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(PostView)
admin.site.register(Like)
# Register your models here.
