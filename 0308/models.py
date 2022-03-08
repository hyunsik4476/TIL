from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)    # 처음 추가될 때만
    updated_at = models.DateTimeField(auto_now=True)        # 뭔가 바뀔 때 항상
