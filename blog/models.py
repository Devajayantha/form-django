from django.db import models
import os
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=125)
    content = models.TextField()
    short_content= models.TextField()
    created_at =models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    content = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_at =models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

class Upload(models.Model):
    title_pic = models.CharField(max_length=255)
    model_pic = models.ImageField(upload_to ='images/')
    def __str__(self):
        return self.title_pic
