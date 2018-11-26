from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class UserAccount(models.Model):
    '''Model Representing User'''
    user = models.OneToOneField(User, default=False, on_delete=models.CASCADE)
    friend_code = models.CharField(max_length=20)
    friends = models.ManyToManyField('UserAccount', blank=True, default=None, symmetrical=True)

    def __str__(self):
        return self.user.username

    def display_friends(self):
        return ", ".join(friend.user.username for friend in self.friends.all())


class Post(models.Model):
    """Model Representing a Post"""
    author = models.ForeignKey('UserAccount', on_delete=models.CASCADE)
    text_content = models.TextField(max_length= 500, help_text = 'Whats on your mind?',default= 'SOME_TEXT')
    img_content = models.ImageField(upload_to =None,height_field=None,width_field=None,max_length=100, default='SOME_IMG')
    time_stamp = models.DateTimeField(blank=True, auto_now_add=False) #Changed auto_now_add from True to False for mock data

    def __str__(self):
        return f"{self.author}, {self.time_stamp}"


class Comment(models.Model):
    content = models.TextField(max_length=250)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    author = models.ForeignKey('UserAccount', on_delete=models.CASCADE)
    time_stamp = models.DateTimeField(blank=True, auto_now_add=False) #Changed auto_now_add from True to False for mock data

    def __str__(self):
        return f"{self.author}, {self.time_stamp}"


class Reaction(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE, default = None)
    user = models.ForeignKey('UserAccount', on_delete=models.CASCADE, default = None)
    time_stamp = models.DateTimeField(blank=True, auto_now_add=False) #Changed auto_now_add from True to False for mock data

    REACTIONS = (('0', 'None'),
    ('1', 'React 1'),
    ('2', 'React 2'),
    ('3', 'React 3'),
    ('4', 'React 4'))
    status = models.CharField(max_length=1,choices= REACTIONS,blank=True,default= '0')

    def __str__(self):
        return f"{self.user}, {self.time_stamp}, {self.status}"
