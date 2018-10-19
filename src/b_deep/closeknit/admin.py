from django.contrib import admin
from closeknit.models import User, Post, Comment, Reaction

# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    model = User
    list_display = ("first_name","last_name","username","email","friend_code","display_friends")

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    model = Post
    list_display = ("author", "time_stamp", "text_content", "img_content")

@admin.register(Comment)
class PostAdmin(admin.ModelAdmin):
    model = Comment
    list_display = ("author", "time_stamp", "content")

@admin.register(Reaction)
class PostAdmin(admin.ModelAdmin):
    model = Reaction
    list_display = ("user", "time_stamp", "status")
