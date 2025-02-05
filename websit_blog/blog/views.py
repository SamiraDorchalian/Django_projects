from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.views import generic

from .models import Post
from .forms import NewPostForm

# Create your views here.

# def post_list_view(request):
#     # posts_list = Post.objects.all()
#     posts_list = Post.objects.filter(status='pub').order_by('-datetime_modified')
#
#     return render(request, 'blog/posts_list.html', {'posts_list' : posts_list})

class PostListView(generic.ListView):
    # model = Post
    template_name = 'blog/posts_list.html'
    context_object_name = 'posts_list'

    def get_queryset(self):
        return Post.objects.filter(status='pub').order_by('-datetime_modified')

# def post_detail_view(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     # try:
#     #     post = Post.objects.get(pk=pk)
#     # except ObjectDoesNotExist:
#     # # except Post.DoesNotExist:
#     #     post = None
#     #     print('Excepted')
#     return render(request, 'blog/post_detail.html', {'post': post})

class PostDetailView(generic.DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'


def post_create_view(request):
    if request.method == 'POST':
        form = NewPostForm(request.POST)
        if form.is_valid():
            form.save()
            # return redirect(reverse('posts_list'))
            return redirect('posts_list')

    else:
        form = NewPostForm

    return render(request, 'blog/post_create.html', context={'form': form})
    # # print(request.POST)
    # # print(request.POST.get('title'))
    # if request.method == 'POST':
    #     # print(request.POST.get('title'))
    #     # print(request.POST.get('text'))
    #     post_title = request.POST.get('title')
    #     post_text = request.POST.get('text')
    #
    #     user = User.objects.all()[0]
    #     Post.objects.create(title=post_title, text=post_text, author=user, status='pub')
    # else:
    #     print('GET request')
    # return render(request, 'blog/post_create.html')

def post_update_view(request, pk):
    # post = Post.objects.get(pk:pk)
    post = get_object_or_404(Post, pk=pk)
    form = NewPostForm(request.POST or None, instance=post)

    if form.is_valid():
        form.save()
        return redirect('posts_list')

    return render(request, 'blog/post_create.html', context={'form': form})


def post_delete_view(request ,pk):
    post = get_object_or_404(Post, pk=pk)

    if request.method == 'POST':
        post.delete()
        return redirect('posts_list')

    return render(request, 'blog/post_delete.html', context={'post': post})
