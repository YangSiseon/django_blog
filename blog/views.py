from django.shortcuts import render, get_object_or_404, redirect
from blog.models import Blog
from django.utils import timezone
def home(request):
    content = Blog.objects
    return render(request, 'home.html',{'blogs':content})

def detail(request, blog_id):
    content = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'detail.html',{'blogs':content})

def new(request):
    return render(request, 'new.html')

def create(request):
    blog = Blog()
    blog.title = request.GET['title']
    blog.body = request.GET['body']
    blog.pub_date = timezone.datetime.now()
    blog.save()
    return redirect('/blog/'+str(blog.id))
# Create your views here.
