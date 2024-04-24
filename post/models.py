from django.db import models

from user.models import UserModel

# Create your models here.
class PostModel(models.Model):
    class Meta:
        db_table = "post"
    
    title = models.CharField(max_length=100, null=False)
    content = models.TextField()
    author = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    