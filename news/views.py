from django.shortcuts import render, get_object_or_404
from .models import Post

# Create your views here.
def index(request):
    posts = Post.objects.all()
    context ={
        'title': 'This is the homePage',
        'posts':posts
    }
    return render(request, 'index.html', context)

def detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    context = {
        'post':post,
    }
    
    return render(request, 'detail.html', context)


def about(request):
    context = {
        "title": 'My Story'
    }
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')


