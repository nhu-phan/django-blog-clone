from curses.ascii import HT
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic import (TemplateView, ListView, DetailView, CreateView, 
                                    UpdateView, DeleteView)
from blog.models import Post, Comment
from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin
from blog.forms import PostForm, CommentForm, RegisterForm
from django.http import HttpResponse
from django.contrib.auth import login
from django.contrib.auth.models import User


class AboutView(TemplateView):
    template_name = 'about.html'
    

class PostListView(ListView):
    model = Post

    def get_queryset(self):
        return Post.objects.filter(published_date__lte =timezone.now()).order_by('-published_date')
        # get query set - sql query on the model
        # grab all objects in post model and filter based on the conditions
        # grab the published date __field_condition (search upp field lookup)
        # lte = less than or equal to
        # so grab the published dates that are equal or less than current time and order them 
        # by publised date ==> -published_date order in descending order (recent post comes first)
   
class PostDetailView(DetailView):
    model = Post
    
class PostUpdateView(UpdateView, LoginRequiredMixin):
    login_url = '/login/'
    redirect_field_name = 'blog/post_detail.html' # redirect to detail view
    form_class = PostForm
    model = Post

class PostDeleteView(LoginRequiredMixin,DeleteView):
    model = Post
    # success url where to go when post is deleted
    success_url = reverse_lazy('post_list') # home page view name, check views.py

class DraftListView(ListView,LoginRequiredMixin):
    model = Post
    login_url = '/login/'
    redirect_field_name = 'blog/post_list.html'

    def get_queryset(self):
        return Post.objects.filter(published_date__isnull = True).order_by('create_date')

@login_required    
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/comment_form.html', {'form': form, 'toEdit': False }) # return to comment form page

############################################################################
############################################################################
############################################################################
# get_object_or_404  calls the given model and get object from that 
# if that object or model doesn't exist it raise 404 error.
@login_required #make this entire view visible to users who are logged ion
def add_comment_to_post(request, pk):
    post = get_object_or_404(Post,pk=pk)
    # using the pk we passed in as the param, we call the function to get the obj
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'blog/comment_form.html', {'form': form, 'toEdit': False }) # return to comment form page
            
@login_required            
def approving_comment(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('post_detail', pk=comment.post.pk) # returning to the post of the comment

@login_required
def removing_comment(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    post_pk = comment.post.pk
    comment.delete() # deleting from the database
    return redirect('post_detail', pk=post_pk)

@login_required
def publishing_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('post_detail', pk = post.pk)

def view_base(request):
    return render(request, 'blog/base.html', {})

def see_you_again(request):
    return render(request, 'seeyou.html', {})

def register_request(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('post_list')
    else:
        form = RegisterForm()
    print(form.errors)
    return render(request, template_name='blog/register_form.html', context={'form':form})
