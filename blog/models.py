from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

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


    def __str__(self):
        return self.subtitle
