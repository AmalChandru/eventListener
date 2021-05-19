from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Post


def home(request):
    context = {
    'posts' : Post.objects.all()
    }
    return render(request, 'eventPortal/home.html', context)

class PostListView(ListView):
    model = Post
    template_name = 'eventPortal/home.html'
    context_object_name = 'posts'
    ordering = ['date_posted']

class PostDetailView(DetailView):
    model = Post

class PostCreateView(CreateView):
    model = Post
    fields = ['title', 'content']

def about(request):
    return render(request, 'eventPortal/about.html',{'title': 'About'})

