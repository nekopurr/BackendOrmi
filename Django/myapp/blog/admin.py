from django.contrib import admin
from .models import Post, Comment, HashTag # model 임포트

# Register your models here.
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(HashTag)