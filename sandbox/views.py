from django.views.generic import (
    TemplateView, ListView, DetailView
)
from django.views.generic.edit import (
    CreateView, UpdateView, DeleteView
)

from .models import Post


class HomeView(TemplateView):
    template_name = 'sandbox/home.html'


class PostListView(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'sandbox/post_list.html'


class PostDetailView(DetailView):
    model = Post
    context_object_name = 'post'
    template_name = 'sandbox/post_detail.html'


class PostCreateView(CreateView):
    model = Post


class PostUpdateView(UpdateView):
    model = Post


class PostDeleteView(DeleteView):
    model = Post
