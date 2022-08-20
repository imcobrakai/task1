from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='posts')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    summary = models.CharField(max_length=255)
    content = models.TextField()
    draft = models.BooleanField(default=False)
