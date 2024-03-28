from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from django_comments.moderation import CommentModerator, moderator

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    create_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name


class Post(models.Model):
    subtitle = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    content = models.TextField()
    publish = models.BooleanField(default  = True)
    author = models.ForeignKey(User, on_delete=models.CASCADE , blank=True, null=True)
    category = models.ManyToManyField(Category)
    image = models.ImageField(upload_to='images/%d-%M-%Y/', blank=True, null=True)
    create_date = models.DateTimeField(default=timezone.now)
    enable_comment = models.BooleanField(default=True)


    def __str__(self): #type ignore
        return self.subtitle


class PostCommentModerator(CommentModerator):
    enable_field = "enable_comment"


moderator.register(Post, PostCommentModerator)

class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        result = self.post.name + " liked by " + self.user.username
        return result
    
