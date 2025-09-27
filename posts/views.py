from django.urls import reverse_lazy
from django.views.generic import (ListView , DetailView, CreateView, DeleteView, UpdateView)            # Import necessary generic views
from .models import Post, Status                                                                        # Import the Post model and Status model
from django.contrib.auth.models import User                                                             # Import the User model
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin                          # Import mixins for authentication and authorization

# Create your views here.
# List view for displaying all posts
class PostListView(ListView):
    #model = Post
    template_name = 'posts/list.html'
    context_object_name = 'post_list'
    ordering = ['-created_on']  # Order posts by creation date, newest first
    status = Status.objects.get(name="published")
    queryset = Post.objects.filter(status=status).order_by('-created_on')
    
class PostDraftListView(LoginRequiredMixin, ListView):
    #model = Post
    template_name = 'posts/drafts.html'
    context_object_name = 'post_drafts'
    ordering = ['-created_on']  # Order draft posts by creation date, newest first
    status = Status.objects.get(name="draft")
    queryset = Post.objects.filter(status=status).order_by('-created_on')   
    
    def get_context_data(self, **kwargs): #To filter drafts by logged in user
        context = super().get_context_data(**kwargs)
        draft_posts = context['post_drafts'].filter(author=self.request.user)
        context['post_drafts'] = draft_posts
        return context
    
class PostArchivedListView(LoginRequiredMixin, ListView): 
    #model = Post
    template_name = 'posts/archived.html'
    context_object_name = 'post_archived'
    ordering = ['-created_on']  # Order Archived posts by creation date, newest first
    status = Status.objects.get(name="archived")
    queryset = Post.objects.filter(status=status).order_by('-created_on')   
    
    def get_context_data(self, **kwargs): #To filter archived by logged in user
        context = super().get_context_data(**kwargs)
        archive_posts = context['post_archived'].filter(author=self.request.user)
        context['post_archived'] = archive_posts
        return context  
    
# Detail view for displaying a single post
class PostDetailView(LoginRequiredMixin, DetailView):
    model = Post
    template_name = 'posts/detail.html'
    context_object_name = 'single_post'
    
# Create view for creating a new post
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'posts/new.html'
    fields = ['title', 'subtitle', 'body', 'status']
    success_url = reverse_lazy('posts')  # Redirect to the posts list after creation

    def form_valid(self, form):
        form.instance.author = self.request.user  # Set the author to the logged-in user
        return super().form_valid(form)
    
# Delete view for deleting a post
class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'posts/delete.html'
    success_url = reverse_lazy('posts')  # Redirect to the posts list after deletion
    
# Update view for editing a post
class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    template_name = 'posts/edit.html'
    fields = ['title', 'subtitle', 'body', 'status']
    success_url = reverse_lazy('posts')  # Redirect to the posts list after updating