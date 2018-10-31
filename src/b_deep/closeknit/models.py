from django.db import models
from datetime import datetime


# Create your models here.
class UserAccount(models.Model):
    '''Model Representing User'''
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=254, unique=True)
    username = models.CharField(max_length=20) # Removed unique=True for mock data
    friend_code = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    friends = models.ManyToManyField('UserAccount', blank=True, default=None, symmetrical=True)

    def __str__(self):
        return self.username
    
    def display_friends(self):
        return ", ".join(friend.username for friend in self.friends.all())



    
class Post(models.Model):
    """Model Representing a Post"""
    author = models.ForeignKey('UserAccount', on_delete=models.CASCADE)
    text_content = models.TextField(max_length= 500, help_text = 'Whats on your mind?',default= 'SOME_TEXT')
    img_content = models.ImageField(upload_to =None,height_field=None,width_field=None,max_length=100, default='SOME_IMG')
    time_stamp = models.DateTimeField(blank=True, auto_now_add=False) #Changed auto_now_add from True to False for mock data

    def __str__(self):
        return f"{self.author}, {self.time_stamp}"

    def num_react_1(self):
        if ( self.reaction_set.all().count() == 0 ):
            return 25
        return max(1, self.reaction_set.filter(status='1').count() / self.reaction_set.all().count() * 100)

    def num_react_2(self):
        if ( self.reaction_set.all().count() == 0 ):
            return 25
        return max(1, self.reaction_set.filter(status='2').count() / self.reaction_set.all().count() * 100)

    def num_react_3(self):
        if ( self.reaction_set.all().count() == 0 ):
            return 25
        return max(1, self.reaction_set.filter(status='3').count() / self.reaction_set.all().count() * 100)

    def num_react_4(self):
        if ( self.reaction_set.all().count() == 0 ):
            return 25
        return max(1, self.reaction_set.filter(status='4').count() / self.reaction_set.all().count() * 100)


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
        return f"{self.user}, {self.time_stamp}"


