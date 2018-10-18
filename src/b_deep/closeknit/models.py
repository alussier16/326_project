from django.db import models
from datetime import datetime


# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=30, default= 'SOME_NAME')
    last_name = models.CharField(max_length=30, default = 'SOME_NAME')
    username = models.CharField(max_length=20, unique=True)
    friend_code = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    friends = models.ManyToManyField('User', blank=True, default=None, symmetrical=True)

    def __str__(self):
        return self.username
    
    def display_friends(self):
        return ", ".join(friend.username for friend in self.friends.all())


    
class Post(models.Model):
    """Model Representing a Post"""
    author = models.ForeignKey('User', on_delete=models.CASCADE)
    text_content = models.TextField(max_length= 500, help_text = 'Whats on your mind?',default= 'SOME_TEXT')
    img_content = models.ImageField(upload_to =None,height_field=None,width_field=None,max_length=100, default='SOME_IMG')
    time_stamp = models.DateTimeField(blank =True, default='2018-10-17T23:02:30Z')
    def __str__(self):
        return self.user.username
    
    

class Comment(models.Model):
    content = models.TextField(max_length=250)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    time_stamp = models.DateTimeField(blank =True, default='2018-10-17T23:02:30Z')

    def __str__(self):
        return self.user.username


class Reaction(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE, default = None)
    user = models.ForeignKey('User', on_delete=models.CASCADE, default = None)

    REACTIONS = (('0', 'None'),
    ('1', 'React 1'),
    ('2', 'React 2'), 
    ('3', 'React 3'),
    ('4', 'React 4'),
    ('5', 'React 5'))
    status = models.CharField(max_length=1,choices= REACTIONS,blank=True,default= '0')


