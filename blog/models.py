from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=125)
    content = models.TextField()
    short_content= models.TextField()
    created_at =models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)


class Comment(models.Model):
    content = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_at =models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)