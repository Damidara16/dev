from django.db import models
from accounts.models import Author
from django.contrib.auth.models import User

class Post(models.Model):
    content = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100)
    #color = models.CharField(max_length=15, null=True)
    #colors = models.CharField(max_length=155, default='blue')
    private = models.BooleanField(default=False)
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.title + ' - ' + self.author.username

class waste(models.Model):
    yes = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)


class Comments(models.Model):
    comment_post = models.ForeignKey(Post, on_delete=models.CASCADE)
    context = models.CharField(max_length=255)
    user = models.ForeignKey(User)
    comment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username + ' - ' + self.comment_date

'''name of the user who posted the comment and comment date'''
