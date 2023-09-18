from django.shortcuts import render,get_object_or_404
from .models import Category,Post
# Create your views here.
def index(request):
    posts = Post.objects.all()
    return render(request, 'index.html',{'posts':posts})

def single(request, id):
  
        post = get_object_or_404(Post, pk=id)
        context = {"post": post}
        return render(request, 'single.html', context)
