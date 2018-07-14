from django.shortcuts import render,get_object_or_404
from django.conf.urls import url
from .models import Post,Comment
from .forms import CommentForm
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage,\
    PageNotAnInteger



def post_list(request):
    posts = Post.objects.all()
    return render(request,'list.html',{'posts': posts})

def post_detail(request, year, month, day, post):
    #post = get_object_or_404(Post, slug=post,status='published', publish__year=year, publish__month=month,publish__day=day)
    #post=Post(title="test123")
    post=Post.objects.get(pk=1)
    comments = post.comments.filter(active=True)
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
    else:
        comment_form = CommentForm()

    return render(request,'details.html',{'post': post , 'comments': comments,'comment_form':comment_form})