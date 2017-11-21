from django.shortcuts import render
from django.http import HttpResponse, Http404
from blog.models import Article
from datetime import datetime

def Test(request):
    # post = Article.objects.all()
    # return HttpResponse(post[0].content)
    return render(request, 'blog/test.html', {'current_time': datetime.now()})

def home(request):
    post_list = Article.objects.all()
    return render(request, 'blog/home.html', {'post_list': post_list})
# Create your views here.

def Detail(request, id):
    try:
        post = Article.objects.get(id=str(id))
    except Article.DoesNotExist:
        raise Http404
    return render(request, 'bloh/post.html', {'post': post})
