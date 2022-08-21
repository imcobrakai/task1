from django.db import models
from django.contrib.auth import get_user_model

user = get_user_model()

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='posts')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category')
    summary = models.CharField(max_length=255)
    content = models.TextField()
    draft = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(user, on_delete=models.CASCADE)