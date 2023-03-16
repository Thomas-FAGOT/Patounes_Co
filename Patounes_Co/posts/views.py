from django.shortcuts import render

from .models import Post

# Create your views here.

def index(request):
    posts = Post.objects.all()
    posts_number = posts.count()

    message = f'{posts_number} posts :'
    if posts_number == 1:
        message = f'{posts_number} post :'
    
    context = {
        'posts': posts,
        'message': message,
    }
    return render(request, 'posts/index.html', context)