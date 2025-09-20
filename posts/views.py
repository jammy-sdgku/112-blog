from django.urls import reverse_lazy
from django.views.generic import (ListView , DetailView, CreateView, DeleteView, UpdateView)
from .models import Post
from django.contrib.auth.models import User

# Create your views here.
# List view for displaying all posts
class PostListView(ListView):
    model = Post
    template_name = 'posts/list.html'
    context_object_name = 'post_list'
    ordering = ['-created_on']  # Order posts by creation date, newest first
    
# Detail view for displaying a single post
class PostDetailView(DetailView):
    model = Post
    template_name = 'posts/detail.html'
    context_object_name = 'single_post'
    
# Create view for creating a new post
class PostCreateView(CreateView):
    model = Post
    template_name = 'posts/new.html'
    fields = ['title', 'subtitle', 'body']
    success_url = reverse_lazy('posts')  # Redirect to the posts list after creation

    def form_valid(self, form):
        form.instance.author = User.objects.filter(is_superuser=True).first()
        return super().form_valid(form)
    
# Delete view for deleting a post
class PostDeleteView(DeleteView):
    model = Post
    template_name = 'posts/delete.html'
    success_url = reverse_lazy('posts')  # Redirect to the posts list after deletion
    
# Update view for editing a post
class PostUpdateView(UpdateView):
    model = Post
    template_name = 'posts/edit.html'
    fields = ['title', 'subtitle', 'body']
    success_url = reverse_lazy('posts')  # Redirect to the posts list after updating