from django.contrib import admin
from django.contrib.auth.models import User
from closeknit.models import UserAccount, Post, Comment, Reaction

# Register your models here.
@admin.register(UserAccount)
class UserAdmin(admin.ModelAdmin):
    model = UserAccount
    list_display = ("__str__", "friend_code","display_friends")

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    model = Post
    list_display = ("author", "time_stamp", "text_content", "img_content")

@admin.register(Comment)
class PostAdmin(admin.ModelAdmin):
    model = Comment
    list_display = ("author", "post", "time_stamp", "content")

@admin.register(Reaction)
class PostAdmin(admin.ModelAdmin):
    model = Reaction
    list_display = ("user","post", "time_stamp", "status")
