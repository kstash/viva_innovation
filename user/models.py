from django.contrib.auth.models import AbstractUser
# from django.db import models

# Create your models here.
class UserModel(AbstractUser):
    pass
    # class Meta:
    #     db_table = "user"
    
    # name = models.CharField(max_length=20, null=False)
    # email = models.EmailField(max_length=20, null=False)
    # # 비밀번호 규칙은 8자 이상, 소문자, 대문자, 특수문자 각 1자리 이상 포함
    # password = models.CharField(min=8, max_length=20, null=False) 
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)
