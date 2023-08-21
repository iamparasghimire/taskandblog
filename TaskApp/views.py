from typing import Any
from django.urls import reverse_lazy
from django.contrib.auth import login,authenticate
from django.views.generic import FormView
from django.views.generic.edit import CreateView
from django.views.generic import ListView,UpdateView,CreateView,DeleteView,DetailView
from .models import Task,Blog,Userprofile,Comment
from .forms import TaskForm,LoginForm,SignupForm,BlogForm,CommentForm
from django.contrib.auth.views import LogoutView,LoginView
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.contrib.auth.views import (
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView
)
from django.shortcuts import get_object_or_404,render
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required


@login_required
def comment_list(request, pk):
    blog = Blog.objects.get(pk=pk)
    comments = Comment.objects.all()
    form = CommentForm()
    return render(request, 'taskapp/blog_detail.html', {'comments': comments, 'form': form,'blog':blog})




@login_required
def add_comment(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            # Assuming you have the blog instance available, like from the URL parameter 'pk'
            comment.blog = Blog.objects.get(pk=request.POST['blog_id'])  # Adjust this based on your code
            comment.save()
            data = {
                'author': comment.author.username,
                'created_at': comment.created_at.strftime('%Y-%m-%d %H:%M:%S'),
                'content': comment.content
            }
            return JsonResponse(data)
        else:
            return JsonResponse({'error': 'Invalid form data'}, status=400)
    return JsonResponse({'error': 'Bad request'}, status=400)



    




class CustomPasswordResetView(PasswordResetView):
    template_name = 'registration/password_reset_form.html' 
    success_url = reverse_lazy('taskapp:password_reset_done')

class CustomPasswordResetDoneView(PasswordResetDoneView):
    template_name = 'registration/password_reset_done.html' 

class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'registration/password_reset_confirm.html'  
    success_url = reverse_lazy('taskapp:password_reset_complete')  

class CustomPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = 'registration/password_reset_complete.html'  




class LoginView(LoginView):
    template_name = 'taskapp/login.html'
    form_class  =  LoginForm
    success_url = reverse_lazy('taskapp:task_list')

    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('taskapp:task_list')
        return super().get(request, *args, **kwargs)


    def form_valid(self, form):
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username = username,password = password)
        if user is not None:
            login(self.request,user)
        return super().form_valid(form)

class SignupView(FormView):
    template_name = 'taskapp/signup.html'
    form_class  =  SignupForm
    success_url = reverse_lazy('taskapp:login')

    
    
    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('taskapp:task_list')
        return super().get(request, *args, **kwargs)


    def form_valid(self, form):
        user = form.save()
        Userprofile.objects.create(user=user)
        # login(self.request, user)
        return super().form_valid(form)
    





    


class UserProfileView(LoginRequiredMixin,DetailView):
    model = Userprofile
    template_name = 'taskapp/blog.html'  
    context_object_name = 'user_profile'



    
class CustomLogoutView(LogoutView):
    template_name = 'taskapp/logout.html'
    


class TaskListView(LoginRequiredMixin,ListView):
    model = Task
    template_name = 'taskapp/task_list.html'
    context_object_name = 'tasks'

    def get_queryset(self):
        query = self.request.GET.get('q')
        queryset = super().get_queryset()

        if query:
            queryset = queryset.filter(Q(title__icontains = query))

        return queryset


class BlogListView(LoginRequiredMixin,ListView):
    model = Blog
    template_name = 'taskapp/blog.html'
    context_object_name = 'blogs'
    slug_url_kwarg = 'slug'

    def get_queryset(self):
        query = self.request.GET.get('q')
        queryset = super().get_queryset()

        if query:
            queryset = queryset.filter(Q(name__icontains = query))

        return queryset
    



        
class TaskCreateView(LoginRequiredMixin,CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'taskapp/task_form.html'
    success_url = reverse_lazy('taskapp:task_list')

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)

class BlogCreateView(LoginRequiredMixin,CreateView):
    model = Blog
    form_class = BlogForm
    template_name = 'taskapp/blog_form.html'
    success_url = reverse_lazy('taskapp:blog')
    slug_url_kwarg = 'slug'

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)

class TaskUpdateView(LoginRequiredMixin,UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'taskapp/task_form.html'
    context_object_name = 'task'
    success_url = reverse_lazy('taskapp:task_list')
    slug_url_kwarg = 'slug' 


    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        
        if self.object.creator != self.request.user:
            from django.core.exceptions import PermissionDenied
            raise PermissionDenied
            
        return super().dispatch(request, *args, **kwargs)



class BlogUpdateView(LoginRequiredMixin,UpdateView):
    model = Blog
    form_class = BlogForm
    template_name = 'taskapp/blog_form.html'
    context_object_name = 'blog'
    success_url = reverse_lazy('taskapp:blog')
    slug_url_kwarg = 'slug' 


    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        
        if self.object.creator != self.request.user:
            from django.core.exceptions import PermissionDenied
            raise PermissionDenied
            
        return super().dispatch(request, *args, **kwargs)
    

class TaskDeleteView(LoginRequiredMixin,DeleteView):
    model = Task
    template_name = 'taskapp/task_confirm_delete.html'
    context_object_name = 'task'
    success_url = reverse_lazy('taskapp:task_list')
    slug_url_kwarg = 'slug' 


    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        
        if self.object.creator != self.request.user:
            from django.core.exceptions import PermissionDenied
            raise PermissionDenied
            
        return super().dispatch(request, *args, **kwargs)

class BlogDeleteView(LoginRequiredMixin,DeleteView):
    model = Blog
    template_name = 'taskapp/blog_confirm_delete.html'
    context_object_name = 'blog'
    success_url = reverse_lazy('taskapp:blog')
    slug_url_kwarg = 'slug' 

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        
        if self.object.creator != self.request.user:
            from django.core.exceptions import PermissionDenied
            raise PermissionDenied
            
        return super().dispatch(request, *args, **kwargs)




    