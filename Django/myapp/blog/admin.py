from django.contrib import admin
from .models import Post, Comment # model 임포트

# Register your models here.
admin.site.register(Post)
admin.site.register(Comment)