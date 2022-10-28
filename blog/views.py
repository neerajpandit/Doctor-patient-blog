from django.shortcuts import render
from django.views import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from .models import Blog
from .forms import BlogForm
from django.urls import reverse_lazy


class BlogListView(ListView):
    model = Blog
    template_name = 'taskapp/blog_list.html'
    context_object_name = 'bloglist'

class BlogDetailView(DetailView):
    model = Blog
    template_name = 'taskapp/blog_detail.html'
    context_object_name = 'blog'

class BlogCreateView(CreateView):
    success_url = reverse_lazy('blog:blog_list_view')
    template_name = 'taskapp/blog_create.html'
    form_class = BlogForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(BlogCreateView, self).form_valid(form)

class MyBlogListView(ListView):
    model = Blog
    template_name ='taskapp/my_blog.html'
    context_object_name = 'bloglist'
