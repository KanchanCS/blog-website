from django.shortcuts import render,get_object_or_404,redirect
from .models import Category,Post,Like

# Create your views here.
def index(request):
    posts = Post.objects.all()
    return render(request, 'index.html',{'posts':posts})

def single(request, id):
    if request.user.is_authenticated:
        post = get_object_or_404(Post, pk=id)
        user_is_liked = Like.objects.filter(
        post_id=post.id, user=request.user
        ).exists()
        liked_count = 0
        liked_count = Like.objects.filter(post_id=post.id).count()
        context ={
            "post": post,
            "user_is_liked": user_is_liked,
            "liked_count": liked_count,
            }
        return render(request, 'single.html', context)
    else:
        return redirect('account:login')

def like(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    Like.objects.create(post_id=post.id, user=request.user)
    return redirect("blog:single", post.id)


def unlike(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    Like.objects.filter(post_id=post.id, user=request.user).delete()
    return redirect("blog:single", post.id)

    
            
            
