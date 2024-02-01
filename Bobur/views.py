from django.views import View
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin

from Bobur.forms import PostForm, UserLoginForm, UserRegisterModelForm
from Bobur.models import Post

# Create your views here.

class HomePageView(View):
    def get(self, request):
        return render (request, 'html/home.html')
    

class AboutView(View):
    def get(self, request):
        return render (request, 'html/about.html')
    

class LoginView(View):
    def get(self, request):
        form = UserLoginForm()
        return render (request, 'html/login.html', {"form": form})
    
    def post(self, request):
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                print(request.COOKIES)
                messages.success(request, "user successfully logged in")
                return redirect("Bobur:home-page")
            else:
                messages.error(request, "Username or password wrong")
                return redirect("Bobur:login-page")

        else:
            return render(request, "Bobur/login.html", {"form": form})    


class Post_Delete_View(View):
    def get(self, request):
        return render (request, 'html/post_confirm_delete.html')
    

class Post_detailView(View):
    def get(self, request):
        return render (request, 'html/template/post_detail.html')
    

class Post_formvView(View):
    def get(self, request):
        return render (request, 'html/post_form.html')


class RegisterView(View):
    def get(self, request):
        form = UserRegisterModelForm()
        return render (request, 'html/register.html', {'form': form})
    
        
    def post(self, request):
        form = UserRegisterModelForm(data=request.POST)
        if form.is_valid():
            messages.success(request, "User successfully registered")
            form.save()
            return redirect("Bobur:login-page")
        else:
            return render(request, "Bobur/register.html", {"form": form})
    

    
class UserView(View):
    def get(self, request):
        return render (request, 'html/user_posts.html')
    

def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, " Successfully created")
            return redirect('html/create_post.html')
    else:
        form = PostForm()
    return render(request, 'html/create_post.html', {'form': form})

def update_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('html/update_post.html') 
    else:
        form = PostForm(instance=post)
    return render(request, 'html/update_post.html', {'form': form})


