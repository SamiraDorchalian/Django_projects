from django.http import HttpResponse
from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User

from .models import Post


# Create your views here.

def post_list_view(request):
    # posts_list = Post.objects.all()
            #ORM => (Object Relational Mapper)
    posts_list = Post.objects.filter(status='pub') #kwargs
    return  render(request, 'blog/posts_list.html', {'posts_list': posts_list})

def post_detail_view(request, pk):
    post = get_object_or_404(Post, pk=pk)
    # try:
    #     post = Post.objects.get(pk=pk)
    # except ObjectDoesNotExist:
    #     post = None
    #     print('Excepted')
    return render(request, 'blog/post_detail.html', {'post': post})

def post_create_view(request):
    if request.method == 'POST':
        post_title = request.POST.get('title')
        post_text = request.POST.get('text')

        user = User.objects.all()[0]
        Post.objects.create(title=post_title, text=post_text, auther=user, status='pub')
    else:
        print('GET REQUEST')
    return render(request, 'blog/post_create.html')

