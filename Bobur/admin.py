from django.contrib import admin
from .models import User, Post
# Register your models here.


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    pass

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass