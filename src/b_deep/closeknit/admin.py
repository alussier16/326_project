from django.contrib import admin
from closeknit.models import User, Post

# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    model = User
    list_display = ("username", "name", "display_friends")

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    model = Post
