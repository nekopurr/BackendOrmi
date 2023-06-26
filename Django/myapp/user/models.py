from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    email = models.EmailField(unique=True, max_length=255) # unique=True : PK지정
    name = models.CharField(max_length=50, null=True, blank=True) # 비어도 무관하게(null : 0허용, blank : 비어도 ㄱㅊ 보통 두개 같이 씀)
    password = models.CharField(max_length=50)
    registered_date = models.DateTimeField(auto_now_add=True) # 최초 생성 시 한번

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.name