from django.shortcuts import render, get_object_or_404,redirect
from .models import Post
from django.contrib import messages
from django.contrib.auth.models import User
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.contrib.auth.decorators import login_required

def home(request):
    context = {
        'posts':Post.objects.all()
    }
    return render(request,'blog/home.html',context)
def about(request): 
    return render(request,'blog/about.html')
@login_required
def dashboard(request):
    return render(request,'blog/dashboard.html')    

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 2

class PostDetailView(DetailView):
    model = Post  
    template_name = 'blog/detail_view.html'

class PostCreateView(LoginRequiredMixin,CreateView):
    model = Post
    fields=['title','content']    
    template_name='blog/new_post.html'

    def form_valid(self,form):#without a author other user cannot create a post
        form.instance.author = self.request.user
        return super().form_valid(form)
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin,UpdateView):
    model = Post
    fields=['title','content']    
    template_name='blog/update_post.html'
   
   
    def form_valid(self,form):#without author,other user can not update the post
        form.instance.author = self.request.user
        return super().form_valid(form)        

    def test_func(self):
        post = self.get_object()
        if self.request.user== post.author:
            return True
        return False        
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin,DeleteView):
    model = Post
    template_name = 'blog/delete_post.html'
    success_url='/'       

    def test_func(self):
        post = self.get_object()
        if self.request.user== post.author:
            return True
        return False

class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html'  
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')        