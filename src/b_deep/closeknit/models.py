from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=30)
    username = models.CharField(max_length=20, unique=True)
    friend_code = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    friends = models.ManyToManyField('User', blank=True, default=None, symmetrical=True)

    def __str__(self):
        return self.username
    
    def display_friends(self):
        return ", ".join(friend.username for friend in self.friends.all())

class Post(models.Model):
    author = models.ForeignKey('User', on_delete=models.CASCADE)
