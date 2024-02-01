from django.db import models
# from django.contrib.auth.models import AbstractUser


class Post(models.Model):
    title = models.CharField(max_length = 128)
    description = models.TextField()
    avatar = models.ImageField(upload_to='images/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title


class User(models.Model):
    first_name = models.CharField(max_length = 24)
    last_name = models.CharField(max_length = 24)
    post = models.ForeignKey(Post, null = True,  on_delete = models.CASCADE)
    username = models.CharField(unique = True, max_length = 128)
    email = models.EmailField()

    def __str__(self) -> str:
        return self.first_name
